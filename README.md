# voicebox_auto
Voiceboxを使って自動的に合成音声を作成するアプリケーションです。
以下のような形式をCSVファイルを指定すると、それぞれの合成音声を作成できます。
```
utt1,阿部寛はバブル期の不動産投資に失敗し、
utt2,億単位の借金を背負ってしまい、
utt3,仕事も減っていたためピンチに陥るが
utt4,「まだチャンスはある」
utt5,と懸命に働き、20年かけて完済した
utt6,阿部寛は身長が189cmあることから、
utt7,周りの共演者とのバランスがとれず
utt8,仕事が減った時期もあったが、
utt9,自分を小さく見せるために
utt10,カメラから距離を取ったり、座ってみたりなど、
utt11,あらゆる試行錯誤を重ね
utt12,今の地位までのぼりつめた
utt13,仕事が減っていた時期は、やりたくない濡れ場のシーンにも挑戦し
utt14,「自分はこんなにもできるんだ」
utt15,ということをアピールし続けたことで
utt16,シリアスからコメディーまで演じられる役者へと成長し
utt17,数えきれないほどの代表作を抱えるほどの大物俳優となった
```

# 要件
・Voicebox環境
・Python 3.11.6
・Poetry 1.7.1


# Poetry install
```
poeetry install
```

まずはVoiceboxを立ち上げて、以下のURLが表示されるかを確認してください。
http://localhost:50021/docs

# 実行
```
oetry run python src/tts.py --output_dir [output dir] --input_file [input csv]
```
eg.
```
poetry run python src/tts.py --output_dir output/sanma_20241012 --input_file input/sanma_20241012.csv
```