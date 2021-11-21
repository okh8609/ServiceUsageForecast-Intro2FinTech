# ServiceUsageForecast-Intro2FinTech-HW1

## 專案目錄說明
```
.    
├── input          -->  輸入資料    
├── code_analysis  -->  jupyter notebook 用來分析開發用的筆記本    
├── code_run       -->  跑訓練用的執行程式腳本    
├── model          -->  模型保存    
└── submission     -->  提交資料    
```

## 檔案說明
```
.
├── code_analysis
│   ├── GBDT.ipynb             -->  無權重正常訓練版本，有結合32個GBDT    
│   └── GBDT_weighted.ipynb    -->  有權重的訓練版本，結合了32個GBDT        
├── input
│   ├── train.csv              -->  訓練資料    
│   ├── test.csv               -->  測試資料    
│   ├── train_x_pca_umap.csv   -->  月份換數值 / 缺失值填入眾數 / 類別one-hot / 數值常態化 / PCA / UMAP
│   ├── train_y_pca_umap.csv   -->  ..  
│   └── test_x_pca_umap.csv    -->  ..
└── submission
    ├── ensemble_with_umap32.csv                 -->  集成32個預測結果原始資料    
    ├── submission_xgboost_02_with_umap.csv      -->  由交叉驗證模型聯合預測
    ├── submission_xgboost_03_with_umap.csv      -->  由所有資料聯合2個GBDT預測    
    ├── submission_xgboost_03_with_umap32.csv    -->  由所有資料聯合32個GBDT預測     
    ├── ensemble_with_weight.csv                 -->  集成32個預測結果原始資料        
    ├── submission_xgboost_02_with_weight.csv    -->  由交叉驗證模型聯合預測    
    └── submission_xgboost_03_with_weight.csv    -->  由所有資料聯合32個GBDT預測   
```