import requests
import json
import pyaudio
import wave
from pydub import AudioSegment
from io import BytesIO
import argparse
import csv
import os
from tqdm import tqdm  # tqdmのインポート

def vvox_test(text, output_file):
    host = "127.0.0.1"
    port = 50021

    # 音声化する文言と話者を指定（13で標準ずんだもん）
    params = (
        ('text', text),
        ('speaker', 13),
    )

    # 音声合成用のクエリ作成
    query = requests.post(f'http://{host}:{port}/audio_query', params=params)
    query.raise_for_status()

    # 音声合成を実行
    synthesis = requests.post(
        f'http://{host}:{port}/synthesis',
        headers={"Content-Type": "application/json"},
        params=params,
        data=json.dumps(query.json())
    )
    synthesis.raise_for_status()

    # 音声データを取得
    voice = synthesis.content

    # pydubで音声を処理し、最初の0.1秒を削除
    audio = AudioSegment.from_file(BytesIO(voice), format="wav")
    trimmed_audio = audio[100:]

    # トリミング後の音声をファイルに保存
    trimmed_audio.export(output_file, format="wav")

    # 再生処理
    pya = pyaudio.PyAudio()
    stream = pya.open(format=pyaudio.paInt16, channels=1, rate=24000, output=True)

    # トリミング後の音声をバイト列として再生
    stream.write(trimmed_audio.raw_data)
    stream.stop_stream()
    stream.close()
    pya.terminate()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    # 受け取る引数を追加
    parser.add_argument('--output_dir', required=True)
    parser.add_argument('--input_file', required=True)
    args = parser.parse_args()

    output_dir = args.output_dir
    input_file = args.input_file

    # output_dir が存在しない場合は作成
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # 入力ファイルの行数をカウントして進捗バーを設定
    with open(input_file) as f:
        lines = f.readlines()

    # tqdmで進捗バーを表示しながら処理を実行
    for utt_line in tqdm(lines, desc="Processing", unit="utterance"):
        utt_id, utt_text = utt_line.strip().split(",", 1)  # 1つのカンマで分割
        wav_file_path = os.path.join(output_dir, f"{utt_id}.wav")
        vvox_test(utt_text, wav_file_path)
