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
└── input
    ├── train.csv              -->  訓練資料    
    ├── test.csv               -->  測試資料    
    ├── train_x_pca_umap.csv   -->  月份換數值 / 缺失值填入眾數 / 類別one-hot / 數值常態化 / PCA / UMAP
    ├── train_y_pca_umap.csv   -->  ..  
    └── test_x_pca_umap.csv    -->  ..

.
└── submission
    ├── submission_xgboost_03_with_umap32.csv   --> (0.73210)(2.) one-hot / pt / pca / umap
    ├── submission_xgboost_03_with_weight.csv   --> (0.72762)(5)  one-hot / pt / pca / umap / weight
    ├── submission_xgboost_03_with_tsne.csv     --> (0.73116)(3)  one-hot / pt / pca / umap / tsne
    ├── submission_xgboost_03_with_weight2.cs   --> (0.72935)(4)  one-hot / pt / pca / umap / tsne / weight
    ├── submission_xgboost_03_without_pt.csv    --> (0.72715)(6)  one-hot / pca / umap / tsne  
    └── submission_xgboost_03_without_tsne.cs   --> (0.73257)(1.) one-hot / pca / umap
```

## 環境安裝
```
conda create --name py37 python=3.7
conda activate py37

pip install umap-learn
pip install bhtsne
pip install xgboost
pip install scikit-learn
pip install numpy
pip install pandas
pip install scipy
```