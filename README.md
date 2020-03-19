# big data
repo for big data project

在"main" 和 "data preproce" 中，是這次專案的測試程式，將每個函式都確定清楚，而“modeltest”則是第一版程式碼，並建了個基本的模型，簡單的測試了先前寫到的函式，“fianl_project”是最終版本將函式做優化，也將一些經過討論後認為對於本次資料及並不會有幫助的函式去除。

在最一開始的程式碼中"data preproce"裡面有
-def load_row_dataset
-def missing_value
-def normalize
-def buildTrain
-def shuffle
-def splitData
-def buildModel

缺失直的處理一開始是採用直接將最鄰近的直補上，因為這次資料集與時間序列相關，鄰近的直不但可能存在關聯，直也很有可能相近。而原本程式碼是自己寫的，後來發現“fillna”，能更快填上缺失職。

數據的正規化，由於這次資料集的每一項數值的範圍都不一樣，有的甚至差異極大，為了避免訓練上因為不同項數值的差異導致分析其重要性時有誤差，進而使最後結果準確度將低，將數值都調製同一範圍。後來使用sklearn的MinMaxScaler調整。

數據的洗亂及切分，因為真正做最後訓練時資料集量足夠後來並未使用。

# ref

RNN & lstm

https://brohrer.mcknote.com/zh-Hant/how_machine_learning_works/how_rnns_lstm_work.html


tensorflow 2.0 

https://www.tensorflow.org/api_docs/python/tf

https://www.itread01.com/content/1563621603.html

https://iter01.com/176418.html



