# MLearn4CJ - 仓颉机器学习库

<p align="center">
  <strong>A comprehensive machine learning library for Cangjie language</strong><br>
  <em>专为仓颉语言设计的机器学习库</em>
</p>

<p align="center">
<img alt="" src="https://img.shields.io/badge/build-pass-brightgreen" style="display: inline-block;" />
<img alt="" src="https://img.shields.io/badge/cjc-v1.0.4-brightgreen" style="display: inline-block;" />
<img alt="" src="https://img.shields.io/badge/cjcov-NA-red" style="display: inline-block;" />
<img alt="" src="https://img.shields.io/badge/project-open-brightgreen" style="display: inline-block;" />
</p>

## 📖 简介

MLearn4CJ 是一个全面的机器学习库，专为仓颉（Cangjie）语言设计。它包含了丰富的机器学习算法，涵盖分类、回归、聚类、降维、神经网络等领域。

## ✨ 特性

- 🎯 **监督学习**: 线性模型、决策树、集成方法、支持向量机、朴素贝叶斯、K近邻
- 🔮 **无监督学习**: K-Means、DBSCAN、层次聚类、高斯混合模型
- 📉 **降维算法**: PCA、SVD、NMF、LDA、ICA、因子分析
- 🧠 **神经网络**: 多层感知机（MLP）分类器和回归器，支持多种优化器和层类型
- 🔬 **高斯过程**: 高斯过程回归和分类，多种核函数
- 📊 **流形学习**: t-SNE、MDS、Isomap、LLE、谱嵌入
- 🔧 **数据预处理**: 标准化、归一化、编码器、多项式特征
- 📐 **特征选择**: 方差阈值、SelectKBest、RFE、顺序特征选择
- 📏 **模型评估**: 分类指标、回归指标、聚类指标、距离度量
- ⚙️ **模型选择**: 交叉验证、数据分割、参数网格

## 📦 模块结构

```
mlearn4cj/
├── core/               # 核心模块（矩阵运算、线性代数）
├── linear_model/       # 线性模型
├── tree/               # 决策树
├── ensemble/           # 集成方法
├── svm/                # 支持向量机
├── neighbors/          # 近邻算法
├── naive_bayes/        # 朴素贝叶斯
├── cluster/            # 聚类算法
├── decomposition/      # 降维/矩阵分解
├── neural_network/     # 神经网络
├── gaussian_process/   # 高斯过程
├── manifold/           # 流形学习
├── preprocessing/      # 数据预处理
├── feature_selection/  # 特征选择
├── model_selection/    # 模型选择
├── metrics/            # 评估指标
└── utils/              # 工具函数
```

## 🚀 快速开始

### 安装

确保已安装仓颉 SDK，然后在项目中引用 MLearn4CJ：

```toml
# cjpm.toml
[dependencies]
mlearn4cj = { path = "path/to/mlearn4cj" }
```

### 基本使用

#### 线性回归

```cangjie
import mlearn4cj.core.*
import mlearn4cj.linear_model.*

// 创建数据
var X = Matrix(5, 1)
X.set(0, 0, 1.0)
X.set(1, 0, 2.0)
X.set(2, 0, 3.0)
X.set(3, 0, 4.0)
X.set(4, 0, 5.0)

let y = [3.0, 5.0, 7.0, 9.0, 11.0]  // y = 2x + 1

// 训练模型
var model = LinearRegression()
model.fit(X, y)

// 预测
var XTest = Matrix(1, 1)
XTest.set(0, 0, 6.0)
let pred = model.predict(XTest)  // 预测值约为 13.0

// 评估
let r2 = model.score(X, y)
println("R² Score: ${r2}")
```

#### 逻辑回归分类

```cangjie
import mlearn4cj.core.*
import mlearn4cj.linear_model.*

// 创建数据
var X = Matrix(6, 2)
X.set(0, 0, 1.0); X.set(0, 1, 1.0)
X.set(1, 0, 1.5); X.set(1, 1, 1.5)
X.set(2, 0, 2.0); X.set(2, 1, 2.0)
X.set(3, 0, 5.0); X.set(3, 1, 5.0)
X.set(4, 0, 5.5); X.set(4, 1, 5.5)
X.set(5, 0, 6.0); X.set(5, 1, 6.0)

let y: Array<Int64> = [0, 0, 0, 1, 1, 1]

// 训练模型
var model = LogisticRegression(maxIter: 1000, learningRate: 0.1)
model.fit(X, y)

// 预测
let predictions = model.predict(X)
```

#### K-Means 聚类

```cangjie
import mlearn4cj.core.*
import mlearn4cj.cluster.*

// 创建数据
var X = Matrix(6, 2)
// 簇1
X.set(0, 0, 1.0); X.set(0, 1, 1.0)
X.set(1, 0, 1.5); X.set(1, 1, 1.5)
X.set(2, 0, 1.0); X.set(2, 1, 1.5)
// 簇2
X.set(3, 0, 10.0); X.set(3, 1, 10.0)
X.set(4, 0, 10.5); X.set(4, 1, 10.5)
X.set(5, 0, 10.0); X.set(5, 1, 10.5)

// 聚类
var kmeans = KMeans(nClusters: 2, maxIter: 100)
let labels = kmeans.fitPredict(X)

// 获取聚类中心
let centers = kmeans.getCentroids()
```

#### 数据预处理

```cangjie
import mlearn4cj.core.*
import mlearn4cj.preprocessing.*

// 标准化
var scaler = StandardScaler()
let XScaled = scaler.fitTransform(X)

// 逆变换
let XOriginal = scaler.inverseTransform(XScaled)

// Min-Max 缩放
var minmax = MinMaxScaler()
let XMinMax = minmax.fitTransform(X)

// 标签编码
var encoder = LabelEncoder()
let encoded = encoder.fitTransform(["cat", "dog", "cat", "bird"])
```

#### PCA 降维

```cangjie
import mlearn4cj.core.*
import mlearn4cj.decomposition.*

// PCA 降维
var pca = PCA(nComponents: 2)
let XReduced = pca.fitTransform(X)

// 获取解释方差比
let varianceRatio = pca.getExplainedVarianceRatio()
```

#### 模型评估

```cangjie
import mlearn4cj.metrics.*

// 分类指标
let accuracy = ClassificationMetrics.accuracyScore(yTrue, yPred)
let precision = ClassificationMetrics.precisionScore(yTrue, yPred)
let recall = ClassificationMetrics.recallScore(yTrue, yPred)
let f1 = ClassificationMetrics.f1Score(yTrue, yPred)

// 回归指标
let mse = RegressionMetrics.meanSquaredError(yTrue, yPred)
let r2 = RegressionMetrics.r2Score(yTrue, yPred)
let mae = RegressionMetrics.meanAbsoluteError(yTrue, yPred)
```

#### 数据生成

```cangjie
import mlearn4cj.utils.*

// 生成分类数据
let (X, y) = DataGenerator.makeClassification(
    nSamples: 100,
    nFeatures: 10,
    nClasses: 2
)

// 生成回归数据
let (XReg, yReg) = DataGenerator.makeRegression(
    nSamples: 100,
    nFeatures: 5
)

// 生成聚类数据
let (XBlobs, yBlobs) = DataGenerator.makeBlobs(
    nSamples: 100,
    centers: 3
)
```

## 🖐️ 实践案例：手写数字识别

项目包含一个完整的手写数字识别实践案例，位于 `src/test/test_mnist_demo.cj`，展示了如何使用 MLearn4CJ 的神经网络模块进行图像分类任务。

### 案例特点

- **模拟 MNIST 数据**: 使用 `MockMNISTGenerator` 生成模拟的 28×28 像素手写数字图像，无需下载外部数据集
- **神经网络训练**: 使用 `MLPClassifier` 多层感知机进行 10 分类任务（数字 0-9）
- **完整流程**: 包含数据生成、模型创建、训练、评估和可视化全流程
- **优化技术**: 展示了 mini-batch 训练、early stopping 等训练优化技术

### 示例代码

```cangjie
import mlearn4cj.core.*
import mlearn4cj.neural_network.*

// 生成模拟MNIST数据
let (trainImages, trainLabels) = MockMNISTGenerator.generateData(
    numSamplesPerDigit: 30, 
    noiseLevel: 0.15
)

// 创建MLP分类器
// 网络结构: 784 (28x28输入) -> 64 (隐藏层) -> 10 (输出类别)
var mlp = MLPClassifier(
    hiddenLayerSizes: [64],
    activation: ActivationType.ReLU,
    learningRate: 0.05,
    maxIter: 10,
    batchSize: 32,
    earlyStoppingPatience: 3
)

// 训练模型
mlp.fit(trainImages, trainLabels)

// 评估准确率
let accuracy = mlp.score(testImages, testLabels)
println("测试集准确率: ${accuracy * 100.0}%")
```

### 运行测试

```bash
cjpm test
```

测试将自动运行手写数字识别演示，包括小型和中型数据集训练测试。

## 📚 API 参考

### 核心模块 (mlearn4cj.core)

| 类 | 描述 |
|---|---|
| `Matrix` | 矩阵类，支持基本矩阵运算 |
| `MatrixOps` | 矩阵操作工具（点积、归一化、单位矩阵等） |
| `LinearAlgebra` | 线性代数工具（求解、求逆等） |

### 线性模型 (mlearn4cj.linear_model)

| 类 | 描述 |
|---|---|
| `LinearRegression` | 普通最小二乘线性回归 |
| `Ridge` | 带 L2 正则化的岭回归 |
| `Lasso` | 带 L1 正则化的 Lasso 回归 |
| `ElasticNet` | 弹性网络回归（L1 + L2） |
| `LogisticRegression` | 逻辑回归分类器 |
| `SGDClassifier` | 随机梯度下降分类器 |
| `Perceptron` | 感知机分类器 |

### 决策树 (mlearn4cj.tree)

| 类 | 描述 |
|---|---|
| `DecisionTreeClassifier` | 决策树分类器 |
| `DecisionTreeRegressor` | 决策树回归器 |

### 集成方法 (mlearn4cj.ensemble)

| 类 | 描述 |
|---|---|
| `RandomForestClassifier` | 随机森林分类器 |
| `RandomForestRegressor` | 随机森林回归器 |
| `AdaBoostClassifier` | AdaBoost 分类器 |
| `GradientBoostingClassifier` | 梯度提升分类器 |
| `BaggingClassifier` | Bagging 分类器 |
| `VotingClassifier` | 投票分类器 |

### 支持向量机 (mlearn4cj.svm)

| 类 | 描述 |
|---|---|
| `LinearSVC` | 线性支持向量分类器 |
| `SVC` | 支持向量分类器（支持核函数） |
| `SVR` | 支持向量回归器 |
| `Kernels` | 核函数工具类（线性、多项式、RBF、Sigmoid） |

### 近邻算法 (mlearn4cj.neighbors)

| 类 | 描述 |
|---|---|
| `KNeighborsClassifier` | K 近邻分类器 |
| `KNeighborsRegressor` | K 近邻回归器 |
| `RadiusNeighborsClassifier` | 半径近邻分类器 |
| `DistanceUtils` | 距离计算工具 |

### 朴素贝叶斯 (mlearn4cj.naive_bayes)

| 类 | 描述 |
|---|---|
| `GaussianNB` | 高斯朴素贝叶斯 |
| `MultinomialNB` | 多项式朴素贝叶斯 |
| `BernoulliNB` | 伯努利朴素贝叶斯 |

### 聚类 (mlearn4cj.cluster)

| 类 | 描述 |
|---|---|
| `KMeans` | K-Means 聚类 |
| `MiniBatchKMeans` | Mini-Batch K-Means |
| `DBSCAN` | 密度聚类 |
| `AgglomerativeClustering` | 层次聚类 |
| `GaussianMixture` | 高斯混合模型 |

### 降维 (mlearn4cj.decomposition)

| 类 | 描述 |
|---|---|
| `PCA` | 主成分分析 |
| `IncrementalPCA` | 增量 PCA |
| `TruncatedSVD` | 截断 SVD |
| `LinearDiscriminantAnalysis` | 线性判别分析 |
| `NMF` | 非负矩阵分解 |
| `FactorAnalysis` | 因子分析 |
| `FastICA` | 独立成分分析 |

### 神经网络 (mlearn4cj.neural_network)

| 类 | 描述 |
|---|---|
| `MLPClassifier` | 多层感知机分类器 |
| `MLPRegressor` | 多层感知机回归器 |
| `DenseLayer` | 全连接层 |
| `ActivationLayer` | 激活层 |
| `DropoutLayer` | Dropout 层 |
| `BatchNormLayer` | 批归一化层 |
| `Activations` | 激活函数集合（ReLU、Sigmoid、Tanh、Softmax 等） |
| `Losses` | 损失函数集合（交叉熵、MSE 等） |
| `SGDOptimizer` | SGD 优化器 |
| `AdamOptimizer` | Adam 优化器 |

### 高斯过程 (mlearn4cj.gaussian_process)

| 类 | 描述 |
|---|---|
| `GaussianProcessRegressor` | 高斯过程回归器 |
| `GaussianProcessClassifier` | 高斯过程分类器 |
| `RBFKernel` | RBF 核函数 |
| `ConstantKernel` | 常数核函数 |
| `WhiteKernel` | 白噪声核函数 |
| `MaternKernel` | Matern 核函数 |
| `RationalQuadraticKernel` | 有理二次核函数 |

### 流形学习 (mlearn4cj.manifold)

| 类 | 描述 |
|---|---|
| `TSNE` | t-SNE 降维 |
| `MDS` | 多维尺度分析 |
| `Isomap` | 等度量映射 |
| `LocallyLinearEmbedding` | 局部线性嵌入 |
| `SpectralEmbedding` | 谱嵌入 |

### 预处理 (mlearn4cj.preprocessing)

| 类 | 描述 |
|---|---|
| `StandardScaler` | 标准化（Z-score） |
| `MinMaxScaler` | Min-Max 缩放 |
| `MaxAbsScaler` | 最大绝对值缩放 |
| `Normalizer` | 样本归一化 |
| `Binarizer` | 二值化 |
| `PolynomialFeatures` | 多项式特征 |
| `OneHotEncoder` | 独热编码 |
| `LabelEncoder` | 标签编码 |

### 特征选择 (mlearn4cj.feature_selection)

| 类 | 描述 |
|---|---|
| `VarianceThreshold` | 方差阈值选择 |
| `SelectKBest` | 选择 K 个最佳特征 |
| `SelectPercentile` | 按百分比选择特征 |
| `SelectFromModel` | 基于模型选择 |
| `RFE` | 递归特征消除 |
| `SequentialFeatureSelector` | 顺序特征选择 |

### 模型选择 (mlearn4cj.model_selection)

| 类 | 描述 |
|---|---|
| `DataSplitter` | 数据分割（train_test_split） |
| `KFold` | K 折交叉验证 |
| `StratifiedKFold` | 分层 K 折交叉验证 |
| `LeaveOneOut` | 留一交叉验证 |
| `ShuffleSplit` | 随机分割 |
| `TimeSeriesSplit` | 时间序列分割 |
| `RepeatedKFold` | 重复 K 折交叉验证 |
| `GroupKFold` | 分组 K 折交叉验证 |
| `CrossValidator` | 交叉验证器 |
| `ParameterGrid` | 参数网格 |

### 评估指标 (mlearn4cj.metrics)

| 类 | 描述 |
|---|---|
| `ClassificationMetrics` | 分类指标（准确率、精确率、召回率、F1 等） |
| `RegressionMetrics` | 回归指标（MSE、R²、MAE 等） |
| `ClusteringMetrics` | 聚类指标（轮廓系数、CH 指数等） |
| `DistanceMetrics` | 距离度量（欧氏、曼哈顿、余弦等） |

### 工具函数 (mlearn4cj.utils)

| 类 | 描述 |
|---|---|
| `DataGenerator` | 数据生成器（分类、回归、聚类数据） |
| `ShuffleUtils` | 数据混洗 |
| `MathUtils` | 数学工具 |
| `ArrayUtils` | 数组操作 |
| `ValidationUtils` | 数据验证 |
| `Pipeline` | 管道 |
| `MNISTLoader` | MNIST 数据加载器 |

## 🧪 测试

运行测试：

```bash
cd mlearn4cj
cjpm test
```

## 📋 依赖

- 仓颉 SDK >= 1.0.4

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

## 📄 许可证

本项目基于 [Apache License](./LICENSE) ，请自由地享受和参与开源。

## 🙏 致谢

感谢所有为机器学习开源社区做出贡献的开发者们。

---

<p align="center">
  Made with ❤️ for the Cangjie community
</p>
