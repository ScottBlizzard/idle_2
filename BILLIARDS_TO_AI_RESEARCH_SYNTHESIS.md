# From Billiards Reasoning to Falsifiable AI Research Seeds

**整理日期：** 2026-08-26  
**目标会议：** ICLR（以 Oral 级别的反直觉性与机制深度为目标，但不预设能够达到）  
**硬件约束：** 8× NVIDIA RTX 4090，单卡 24 GB；无 NVLink、无显存池化；原则上仅使用 GPU/CPU 仿真与公开数据，不依赖实体机器人  
**工程约束：** 优先选择有公开数据集、公开代码、强 baseline、可在 3–7 天完成杀手实验的方向  
**文档用途：** （1）完整保存台球讨论中的机制；（2）生成互相竞争而非强行合并的 AI 种子；（3）提供可直接交给 Pro 的英文攻击性检索提示词。

---

## 0. 当前结论

这次讨论没有证明一个新理论，也没有授权立即开跑完整项目。它做成了更重要的前置工作：把最初模糊的“通过中间结构减小误差”拆成了若干性质不同的机制，并发现其中至少一个比旧报告中的抽象更反直觉：

> **可恢复、可重复且能够提供校准信息的失败，可能优于一次不可逆的即时成功。**

这句话不能直接作为论文贡献。它很容易与安全探索、可逆 MDP、rollback、active learning、dual control、风险敏感规划、自我纠错、verifier feedback、长期价值和 transactional agents 等文献相撞。它目前只是最值得攻击性检索的研究核。

本轮保留三个互相竞争的种子：

1. **Resettable Failure with Epistemic Progress（可复位失败与认知进步）**：外部任务状态复位，但智能体的知识不复位；多次小额失败可能逐渐逼近安全解，而表面成功可能造成不可逆坏状态。
2. **Diagnosable Control under a Collapsing Robust Action Set（可靠动作集收缩下的可诊断控制）**：动作空间名义维度不等于可用维度；专家优先选择反馈清楚、可重复、可以单变量校准的控制方式，而不是单纯选择容差体积更大的动作。
3. **Macro-Control beyond Point Predictability（点预测失效后的宏观分布控制）**：当微观终态无法稳健预测时，智能体仍可控制宏观事件或结果分布；安全预算耗尽后，最优策略可能从低方差试错切换到高方差脱困。

三个种子不应在没有证据时合并成一篇“大一统”论文。Pro 的任务是优先消灭它们；只有某个种子留下精确的文献空隙、可证伪机制与现实载体，才允许进入实验。

---

## 1. 与现有三份报告的关系

### 1.1 `AI_RESEARCH_REABSTRACTION.md`

该报告的结论是 **NO-GO：re-abstraction 尚未完成**。它证明原始 BFAP 本质上是限制动作维度，以有限预算下的搜索效率换取部分能力，而不是创造新路线。它还指出，真正的 relay、lifted representation、homotopy、skill chaining、semantic DAG、extended formulation 等抽象大多已有成熟文献。

**本轮必须继承的限制：**

- 不能把“中等复杂度最好”“减少无用自由度”“动作平滑化”重新包装成新贡献。
- 不能仅证明受限空间在有限搜索预算下优于完整空间。
- 不能用台球比喻代替 AI 机制与可复现实验。

### 1.2 `AI_RESEARCH_REACHABILITY_EXPANSION.md`

该报告对广义“发现能力不足后增加工具、子目标、表示或控制维度”给出 **NO-GO**。唯一残留是形式化证明中的窄问题 CIPI：局部 progress/value estimator 是否系统性低估结构上必要的 cut/lemma，因而在固定预算下错误剪枝。

**本轮必须继承的限制：**

- “卡住后换工具/加 operator”本身不是贡献。
- adaptive routing、value of computation、hierarchical planning、decomposition 和 test-time compute allocation 已经拥挤。
- 如果新种子落到 theorem proving，必须超越“失败后看 verifier feedback 再试”或“加入 lemma 有帮助”。

### 1.3 `AI_RESEARCH_CARRIER_VIABILITY.md`

该报告对广义“当前成功但损伤未来能力”给出 **NO-GO**。其形式可被 continuation value、viability、attainable utility、impact regularization、persistent memory、rollback 与 transactional execution 覆盖。仅有极窄的“相同当前输出、不同 post-output memory commit 导致未来差异”的因果审计残留，而且也非常拥挤。

**本轮必须继承的限制：**

- 不能仅说“短期成功可能伤害长期价值”。
- 不能仅把失败/成功重新定义成长期 reward。
- 如果使用 rollback 或 persistent memory，必须证明不是普通长程规划、错误传播、memory poisoning 或显然的事务管理。

### 1.4 新讨论真正增加了什么

新内容不是“成功有长期副作用”这一旧结论，而是一个更具体的交互结构：

- 某类动作的**失败分支会把外部状态近似恢复到原点**；
- 智能体在失败过程中获得的观测、校准和可行性判断被保留；
- 因而下一次并不是独立重试，而是在相同外部状态上的认知更新；
- 动作选择还受结果安全硬约束、失败可诊断性、控制变量饱和和风险预算影响；
- 当可恢复重试不再经济时，策略才切换到高方差模式。

是否已有文献把这些性质完整组合并产生非平凡结果，尚未确认。

---

## 2. 台球讨论的完整机制整理

### 2.1 最初的直线摆球：误差减小还是信号一起被消耗

最初设想是在白球、目标球和袋口之间增加中间球。相邻球紧贴时，白球只要打到后球，前球可能沿中心线被传入袋；稍微留间隔后，中间球似乎能增加一定容错。继续摆成直线或曲线，看起来球越多，输入方向误差越容易被“传递结构”吸收。

随后的关键质疑是：如果横向误差和纵向有效动量同时被缩小，只是纵向误差最终落入袋口容差，而有用信号已经被消耗，那么它不是能力增强，只是衰减换稳定。这类结果很可能只是 bias–variance、contractive dynamics、damping 或信息瓶颈的旧故事，论文价值有限。

半圆或曲线摆球也没有自动解决问题。如果预先设定一条曲线把误差导向终点，可能只是人为加入一个稳定项。真正需要区分的是：中间结构是在缩小全部运动、删除自由度，还是创造原系统没有的可行路径。

### 2.2 台球链与机器人手臂的差异：中间结构有时改变可达性

单个白球本来可以从 360° 中试错寻找击打红球的进球点，因此中间加球未必创造新能力。机器人手臂不同：只动手腕可能根本够不到目标；必须先动大臂、小臂，手腕才进入可以调整方向的区域。这里的中间动作不是吸收误差，而是把后续执行器送入新的可达状态。

这个观察后来被旧报告映射成 reachability/operator expansion，但广义表述已被 hierarchical control、options、subgoals、tool use 等覆盖，因此不能直接成为新论文。

### 2.3 斯诺克不是单一“打准”：进球与母球走位是耦合目标

斯诺克至少包含两种能力：

- 把当前目标球打进；
- 控制母球落点，为下一颗球、下下颗球、进攻延续或防守创造局面。

清彩阶段从中球较蓝球是典型例子。若中球被较成直球，当前进球可能简单，但母球的后续方向几乎退化为同一条线：高杆跟进、中杆定住、低杆拉回。为了把蓝球较成继续向下分球的角度，球员通常会主动保留一点角度。

因此“离当前目标更近、更直、更容易”并不等于状态更好。一个当前误差更小的状态，可能让未来可靠控制权急剧下降。

### 2.4 不吃库与吃一库：总误差没有变小，误差方向与好球区域对齐

从中球走蓝球时，不吃库的母球可能沿一条较纵向的直线移动。力度轻一点，蓝球角度太大；重一点，蓝球被较直或较成错误方向。母球的落点误差虽然不一定大，却横穿了一个狭窄的好球区域。

吃一库后，母球路线发生旋转。轻一点或重一点时，落点主要沿着一条较长的“好球走廊”移动；整条线路上的许多点都能舒服地打进蓝球，并继续较下一个彩球。母球物理误差的欧氏长度可能没有变小，路径甚至更长，但误差的主要方向与任务允许方向对齐。

理想库边可以用镜像/展开解释：把球台沿库边反射，多库路径在展开空间中是一条更长的直线。库边不是靠明显吸能来缩小误差；关键是路线几何改变了误差相对于终端接受集合的投影。

真实库边并非理想镜面。恢复系数、球—库摩擦、入射速度和球的旋转共同决定反弹角与反弹速度。库边不会创造总能量，但在某些强旋转条件下，部分旋转能可以转化为平动能，因此只看球心平动速度时可能出现“反弹后似乎更快”的现象；这不能解释为库边无中生有地加速。球—库模型和实验参数可参见 [Mathavan et al., 2010](https://journals.sagepub.com/doi/10.1243/09544062JMES1964)。

这给出第一个稳定抽象：

> 总误差大小不是任务误差。真正重要的是误差在接受集合法向方向上的分量，以及扰动是否沿着等价结果方向传播。

### 2.5 好位置不是点，而是带内外边界的弯曲区域

母球并非越接近目标球越好。太近时，同样的横向位移会造成更大的视觉角度变化；贴库又限制手架和出杆。太远时，瞄准和力度误差累积。好的落点通常是一条有内外边界的弯曲带，而不是单点或以目标球为中心的圆。

因此，用最终坐标 L2 距离评价走位会产生错误排序：沿好球走廊偏离 30 cm 可能仍是好球；横向偏离 5 cm 可能已经失去理想角度。

### 2.6 留角扩大的是可靠控制权，不只是理论可达性

理论上，只要动力足够且不落袋，母球经多库可以到达球台大量区域。但理论可达不等于职业球员愿意在高成功阈值下使用。

直球状态虽然当前简单，却让未来可靠动作集合接近奇异；适当留角后，自然分离角、中高低杆和多库路线共同扩大可稳定到达的区域。强塞也能从直球中“硬凹”一点角度，但需要让点，且塞、力度、偏移和球台状态耦合，可靠可达集远小于理论可达集。

可用如下对象表达：

\[
\mathcal R_\tau(s)=\{y:\exists a,\;\Pr(\text{pot and reach }y\mid s,a)\ge \tau\}.
\]

讨论重点应是高阈值下的可靠可达集，而不是存在某个理想动作就算可达。

### 2.7 多库不等于更复杂：路线长度不是有效控制难度

用户明确给出偏好：“三库自然”经常优于“一库强塞”。这否定了“步骤越多、路径越长就越危险”的朴素度量。

自然三库虽然物理路径长，但每次反弹遵循稳定、熟悉的关系，整体落点区域又可能很宽；一库强塞虽然步骤少，却把多个控制变量耦合在一起，对球杆、力度、台泥和库边参数更敏感。

颗星公式（diamond systems）是职业经验的几何化表达：一库可以用镜像，常见两库、三库可用 Plus、Corner-5 等系统估计。但实际球台仍需根据台速、库边弹性、顺反塞和力量作修正。颗星系统提供的不是一个绝对精确公式，而是一个低维、可快速校准的路线先验。

因此复杂度更接近：

- 控制变量的耦合程度；
- 局部灵敏度；
- 执行噪声；
- 反馈可诊断性；
- 环境校准负担；
- 终端任务接受区域的几何。

### 2.8 正确路线类别可能比局部坐标精度更重要

多库运动会放大理想轨迹的角度误差，但只要选择的路线类别正确，终点在一个很大的区域内都可能是好球。例如某个球型必须绕三库从上半台回到下半台；只要“绕台”这一离散思路正确，偏左偏右一段距离仍在理想区。相反，选择不吃库或错误库数，哪怕短期落点离名义目标更近，也可能完全到不了下一杆的好位置。

这提示应区分：

- 离散的路线/拓扑类别错误；
- 正确类别内部的连续执行误差。

前者可能灾难性，后者可能被任务等价区吸收。评价对象应是任务商空间或结果等价类，而不是原始状态空间中的坐标距离。

### 2.9 加塞是耦合控制，不是免费增加自由度

加塞可以改变吃库后的反弹方向，也可以在被遮挡或角度不足时创造直接击打无法实现的路线。更复杂的扎杆也能进一步改变轨迹。但加塞会带来让点、偏移和力度依赖。

常见加塞方式包括：

- 手架不动，杆尾/杆头形成一定偏转后击打；
- 平移手架，球杆保持较平行的方向击打母球侧面。

同样塞量在小力、中力、大力下的母球偏移和实际吃塞效果不相同，关系不保证全局线性。职业球员熟悉自己的球杆和球台，可以显著降低不确定性，但强塞仍有物理控制上限与更高执行负担。

袋口本身有容错，因此球员有时会“偷点”：不瞄准理论袋口中心，而利用袋口允许范围，为母球走位挤出一点碰撞角度。若直接击打甚至偷点仍无法形成路线，加塞可能通过母球偏转、吃库变化等效应创造更大击打角；扎杆则是更极端的扩展方式。但这些方式都会提高执行、校准和犯错负担，不能被视为免费的能力维度。

### 2.10 球台快速校准：低维系统辨识，但本身很可能不是新方向

职业球员在陌生球台上通常可通过少量球快速判断：

- 台泥偏滑还是偏涩，走球偏快还是偏慢；
- 库边偏软还是偏弹；
- 必要时再判断顺塞、反塞的具体吃库变化。

标准球台提供较强先验，所以只需估计少量残差参数。这很像低维 test-time system identification。它适合作为实验条件或机制组成，但 active system identification、meta-RL、online adaptation 文献成熟，单独成篇大概率不够。

### 2.11 连攻带守：不只最大化进球率，而是寻找进攻集与安全集的交集

简单理想球型下，职业球员通常不会在两个进球率都很高的打法中做抽象的风险选择；位置好就进攻。真正的攻防选择多出现在长台、比分压力、球型遮挡和回球线路受阻时。

某些长台球型天然允许“连攻带守”：按进球方向打时，母球的自然分离角又能回到顶部安全区。球进则获得上手机会；球不进也可能不给对手简单球。这可理解为进攻动作集合与安全动作集合的交集，但该抽象很容易落入 risk-sensitive planning 或 constrained optimization，不足以单独承担论文创新。

防守或走位还必须考虑“只针对母球的障碍”。例如红球十字回球在目标球接触关系上可能成立，但母球反弹回顶部的路线会被其他红球或彩球挡住，导致无法安全回来；这些球并不妨碍当前目标球被击中，却改变了后续载体的可行路径。规划对象因此不是目标球的单条进球线，而是目标球与母球两套碰撞后轨迹的联合可行性。

### 2.12 K 球：不能预测每颗红球，但能控制宏观事件

职业选手会提前把黑球较成适合 K 红球堆的角度。精确预测球堆中每颗红球的终点几乎不现实：微小误差经多球碰撞被放大，碰撞顺序也可能改变。然而选手仍能控制若干宏观目标：

- 黑球或当前红球合法打进；
- 红球堆被有效打开；
- 母球带着足够能量从球堆中走出来，而不是被困住；
- 至少留下可见、可打的下一颗球；
- 避免错误球入袋、黑球被撞死或犯规。

高杆或低杆有时不是为了精确落点，而是保证母球撞入球堆后仍有离开球堆的动力。袋口附近的“保险球”可以提高宏观成功率，但前提仍是母球离开球堆且视线不被新球型遮挡。

这产生一个重要区分：

> 微观终态不可稳健预测，不等于任务相关的宏观事件不可控制。

需要严格限定“不可预测”的含义。理想经典力学在初态和模型完全已知时是确定的，事件驱动模拟可以精确计算球—球和球—库碰撞；参见 [Leckie and Greenspan, 2006](https://journals.sagepub.com/doi/10.3233/ICG-2006-29103)。现实机器面对的则是有限视觉精度、出杆执行噪声、台泥与库边参数误差以及多重接触建模误差。真实机器人台球研究因此把执行后的动作视为概率分布，而非绝对确定输入；参见 [Nierhoff et al., 2016](https://pubmed.ncbi.nlm.nih.gov/26292355/)。多球同时碰撞的真实建模本身也需要复杂的非线性接触模型；参见 [González et al., 2022](https://link.springer.com/article/10.1007/s11071-021-07117-4)。因此后续论文最多应声称“在有限观测与模型精度下，唯一微观终态不具备稳健可预测性”，不能声称物理上存在不可计算的神秘随机性。

K 球可被描述为受约束的随机性注入，但这类表述需要警惕与 stochastic control、distributional RL、robust planning 和 option initiation sets 的直接重合。

### 2.13 K 球的 initiation region：没有舒服角度就不强行启动

选手会先把母球较到一个适合 K 球的角度。如果没有合适的入射区域，通常先把黑球打进，再做防守，而不是强行炸球。说明复杂操作存在 initiation set：只有当前状态落入可靠启动区时，宏观成功概率才足够高。

这一点与 options、viability kernel、precondition learning 和 robust initiation sets 高度相似，单独创新风险很高。

### 2.14 防守的本质：压缩对手的可靠解球空间

评价一杆斯诺克不能只看“遮住了多少”或母球离目标球多远，而要看对手剩余的可靠解球动作集合。

典型优质布置包括：

- 母球靠近库边且被遮挡：手架受限，出杆角度小，力度、杆法和击球点误差增大；
- 需要击打的目标球远离库边：不能直接利用容易估算的贴库颗星路线，解完后也更难保证不留下机会；
- 若目标球本身贴库，镜像/颗星线路可能更容易估计，且目标球被碰后未必形成明显机会。

防守质量至少包含三层：

1. 是否存在合法解法；
2. 有多少解法能在执行误差下稳定碰到目标球；
3. 碰到以后，有多少结果不会给防守方留下进攻机会。

### 2.15 “留一条唯一通道”未必能控制对手结果

最初曾推测：高级防守可能故意给对手留一条明显解法，把对手赶入唯一通道。但用户指出，大多数情况下这很难成立。只要容易解到，对手就可能发力把球打开、多库绕台，甚至反做斯诺克。

几何上的单通道不等于结果上的单通道。容易接触也意味着对手重新获得力度、旋转和碰撞厚度上的控制权。真正需要压缩的是“碰到球以后还能可靠控制多少结果”。

### 2.16 困难但稳的解法：当前成功率低，却可能是全局最优

在高质量斯诺克中，存在两类路线：

- 容易碰到，但碰到后很可能漏球；
- 很难碰到，但只要按该路线执行，无论没碰到还是碰到，通常都不会给对手留下机会。

职业球员可能宁可连续几次没解到、被罚分并复位，也不选择一杆容易碰到但会漏球的路线。这产生了最强反直觉现象：

> 某种“成功”可能比某种“失败”更坏。

这里的失败不是笼统低 reward，而是有特殊结构的小额失败：状态基本保持、防守优势没有交出、规则允许复位并再次尝试。

### 2.17 外部状态复位，内部认知继续：每次罚分购买一次观测

裁判复位通常相当准确。球员第一次没解到后，会根据母球路线判断偏左、偏右、力度不足或塞量不足；复位后沿同一路线修正，通常越来越接近。

因此连续失败不是独立 Bernoulli 重试：

- 球的位置被近似恢复；
- 球员对该路线、该球台和该力度的估计被更新；
- 下一次动作成功率可以提高；
- 每次罚分同时购买了一次校准观测。

若连续尝试表明死活碰不到球，球员会判断这条路线本身可能无解，切换路线。

### 2.18 安全预筛选与在线校准是两个阶段

球员在选择路线之前已经考虑“解到以后是否漏球”。不会先随便解，再从结果判断安全性。更准确的决策顺序是：

1. 预先排除成功后会漏球的路线；
2. 在成功安全、失败也安全的候选中选择路线；
3. 在线校准是否能碰到球；
4. 若控制变量饱和仍碰不到，切换到另一条预先判断为安全的路线。

因此目标近似具有词典序：后果安全是硬约束，接触成功率和少罚分是在安全集合内部优化的次级目标。不过比分会改变这个优先级。

### 2.19 安全预算耗尽后的相变：从可恢复试错切换到高方差脱困

连续罚分并非没有上限。当罚分增加到继续安全试错会直接失去该局希望时，球员会改为大力击球，尽量先碰到目标球，同时争取不留下机会。

此时大力、多库和多球碰撞让最终球型难以预测，局面可能从防守方的确定优势变成接近“五五开”。这不是精确设计随机结果，而是在安全预算耗尽后接受高方差，以避免确定性失败。

可区分三种模式：

- **精确控制：** 状态和控制权充足，追求好球走廊内的稳定终点；
- **可复位试错：** 允许小额失败，利用复位和反馈逐渐校准；
- **高方差脱困：** 低方差路线已不经济，接受微观不可预测性，争取宏观上消除确定劣势。

### 2.20 绝境中名义自由度会坍缩，只剩力度

困难斯诺克中，为了合法碰球且不漏球，方向几乎被几何条件固定，碰撞厚薄也由路线决定，塞未必有可靠空间。最终真正还能主动调节的可能只剩力度。大力击球不是球员自由选择许多随机结果，而是在控制维度被压缩到近似一维时提高“至少碰到”的概率；后续结果主要依赖运气。

这重新接回最初的机器人直觉：系统拥有多少名义自由度，不代表当前约束下拥有多少可靠控制方向。

### 2.21 可靠动作集的维度还不够：方向比力度更容易校准

假设两条安全路线：A 对方向要求极准但力度范围宽，B 方向范围宽但力度必须卡得很窄。用户倾向 A，因为方向是可见的瞄准点，可以用视觉判断并在多次复位后修正；力度主要依赖肌肉感觉，可重复性和精度较差。

因此，动作集合的几何体积或维度不能直接代表难度。每个控制通道还有不同的：

- 感知精度；
- 执行噪声；
- 重复性；
- 反馈延迟；
- 误差符号是否可观察；
- 环境依赖；
- 与其他控制量的耦合。

一个允许区间很窄但反馈清楚的变量，可能比允许区间更宽但只能靠隐性肌肉感觉的变量更容易控制。

### 2.22 自然路线 → 加塞残差 → 换路线：分层控制而非联合盲搜

职业球员通常先选择不加塞的自然反弹。只有自然线路碰不到球时，才逐渐增加塞量；其他条件尽量保持不变，相当于控制变量。若塞加到可靠极限仍碰不到，就判断这类路线不可行，切换另一条路线。

这形成一个清楚的升级顺序：

1. 使用最简单、最稳定、最可诊断的自然动力学；
2. 只在能力不足时加入一个残差控制变量；
3. 在局部近似单调区间内逐步调节；
4. 控制量饱和仍无效时进行离散路线切换，而不是继续硬凹参数。

这比一开始同时联合优化方向、力度、塞量和路线更容易诊断，也更节省试错预算。

### 2.23 局部单调性与有限目标体积：不需要学完整动力学

在力度大致固定时，增加左塞通常让线路持续向左偏，至少在常用工作区间内相对单调。球员无需精确预测完整物理，只需知道“往哪边调”，因为目标球有体积，成功对应一个塞量区间而非唯一参数点。

重复复位下可以做近似 bracket/continuation search：偏右就增加左塞，直到进入接触区间；若达到可靠上限仍未进入，换路线。

### 2.24 物理目标有体积，但任务有效目标由碰撞厚度与力度共同决定

法律意义上，母球碰到目标球任意位置都算解到；但为了不漏球，并非所有碰撞都同样安全。另一方面，如果母球只是轻轻贴到目标球、力度控制合适，传递给目标球的动量很小，那么贴到哪一侧可能都不会留下明显机会。

所以安全接受集合不是目标球表面上的固定弧段，而是接触厚度、入射速度、旋转和后续路线共同形成的联合区域。碰得更薄可能允许稍大速度，碰得更厚需要更小速度。真正的任务变量更接近有效碰撞冲量，而不是单独的接触坐标。

这再次说明：逐维设定独立误差容差会错过补偿关系，接受集合通常是原始动作空间中的弯曲流形或管道。

---

## 3. 从台球中提取的机制词典

| 台球现象 | 非比喻机制 | 容易误写成什么 | 必须控制的旧解释 |
|---|---|---|---|
| 吃库后整条线都是好球 | 扰动沿任务等价方向传播；法向误差小 | “库边吸收误差” | 阻尼、能量衰减、简单鲁棒控制 |
| 离名义点更远却更好 | 评价应在接受集合/任务商空间中进行 | “L2 不好所以换指标” | reward shaping、manifold distance |
| 直球容易但未来难走 | 当前易解状态可能让可靠控制权降秩 | “留角增加自由度” | empowerment、controllability、options |
| 三库自然优于一库强塞 | 步数不是难度；耦合、敏感性和可诊断性更重要 | “长路径反而更好” | action smoothing、system ID、robust MPC |
| K 球无法预测每颗球 | 微观不可预测下仍可控制宏观事件分布 | “混沌也能控制” | distributional RL、stochastic control |
| 难解但安全路线 | 低当前成功率动作可有更好的完整分支结构 | “失败比成功好” | long-horizon value、risk sensitivity |
| 复位后越解越接近 | 外部状态重置、内部信念更新；失败具有信息价值 | “多试几次就好” | active learning、dual control、self-correction |
| 塞加到底仍碰不到 | 连续控制饱和可触发离散策略切换 | “卡住后换工具” | metareasoning、adaptive routing |
| 方向窄但易瞄准 | 几何容差需按通道的感知/执行/反馈噪声加权 | “动作空间越大越容易” | Fisher information、identifiability |
| 罚分多后大力乱局 | 资源预算触发从低方差到高方差策略的相变 | “输的时候就赌博” | risk-seeking utility、desperation strategies |

---

## 4. 三个互相竞争的 AI 研究种子

## Seed A — Resettable Failure with Epistemic Progress

### A.1 核心问题

在允许外部状态准确回滚或自然复位的任务中，智能体能否通过一系列“后果安全但当前失败”的尝试持续积累信息，并优于追求单次成功率的策略？

令系统状态分为外部任务状态 \(x_t\) 与智能体认知状态 \(b_t\)。某个安全尝试 \(a_t\) 失败后：

\[
x_{t+1}\approx x_t,\qquad b_{t+1}=\mathcal U(b_t,o_t),
\]

其中 \(o_t\) 是失败轨迹或 verifier 反馈。失败有成本 \(c_t\)，但不会进入灾难状态。相反，某个高即时成功率动作可能进入不可逆坏状态 \(x_{\mathrm{bad}}\)。

### A.2 反直觉主张候选

> 在总预算相同且每次失败有明确成本时，降低单次成功率、但提高复位精度和反馈信息量的策略，可以提高最终成功率并降低灾难概率；标准的 per-attempt success、myopic value 或把所有失败统一赋负奖励的训练目标会系统性误排这类动作。

更强但更难的版本：

> 当失败返回近似相同的外部状态时，“状态进展为零”不等于“决策进展为零”；忽略认知状态的 evaluator 会把最有价值的轨迹标成无进展。

### A.3 可能的 AI 载体（仅为检索候选）

- 带 snapshot/rollback 的代码代理：失败测试后工作树恢复，但保留诊断与内部记忆；警惕与 self-debugging、SWE-agent、transactional coding、test feedback 和 carrier-viability 报告重合。
- 形式化证明或可验证推理：失败 tactic 保持 proof state，但返回结构化错误；警惕与 proof repair、backtracking、CIPI 和 verifier-guided search 重合。
- 带事务/撤销机制的 GUI、Web 或工具代理：危险动作提交前可在 sandbox 中试运行，失败回滚但保留观测；警惕与 safe exploration、world models、lookahead/rollout 重合。
- 可重复初始化的生成/规划任务：环境种子和任务状态保持，智能体通过带成本 probe 学习隐藏参数；警惕与 active system identification、Bayesian optimization、dual control 重合。

### A.4 最小杀手实验应证明什么

1. 有一类动作在**当前成功率上更低**，但失败分支保持可恢复且产生可测信息。
2. 相同总调用次数、token、GPU 时间和外部成本下，reset-aware 策略最终成功更高或灾难更少。
3. 提升不是普通重采样、best-of-N、更多 compute 或隐藏的 oracle feedback。
4. 移除复位、打乱失败反馈、禁止跨尝试记忆后，优势按预测消失。
5. 存在一类“危险成功”状态，使单纯按当前 verifier/reward 排序确实得到错误政策。

### A.5 最大拒稿风险

- 完整 belief-state MDP 的普通 value function 已经能表达一切。
- Reflexion/self-debugging/active learning 已经说明失败反馈能帮助重试。
- rollback 只是工程事务，失败后重试是显然 baseline。
- “危险成功”只是旧报告中的 long-horizon side effect。

因此 Seed A 只有在找到一个**标准 evaluator 或训练范式的系统性盲点**、一个明确的 phase transition 或一个跨载体可复现的机制签名时才可能存活。

## Seed B — Diagnosable Control under a Collapsing Robust Action Set

### B.1 核心问题

名义动作空间 \(\mathcal A\) 可能高维，但在任务、安全与成功阈值 \(\tau\) 下，可用集合

\[
\mathcal A_{\mathrm{rob}}(s,\tau)
=\{a:\Pr(\text{acceptable outcome}\mid s,a)\ge\tau\}
\]

会变成低维、弯曲甚至不连通的集合。即使两个候选集合体积相近，其控制难度也取决于每个方向的感知噪声、执行噪声和失败反馈可诊断性。

### B.2 反直觉主张候选

> 更大的动作容差或更多名义自由度可能降低有限预算下的可靠控制能力；一个容差更窄但误差符号可见、响应局部单调、可以单变量校准的动作族，可能显著优于容差更宽但反馈不可辨识、变量高度耦合的动作族。

第二个候选：

> 更长的动作序列可以比一步复杂动作更容易控制，前提是长序列由可校准的自然 primitive 构成，而短动作依赖高增益、耦合的残差控制。

### B.3 专家策略结构

1. 先选择自然、低耦合且反馈清楚的 primitive；
2. 只在能力不足时增加一个残差控制维度；
3. 利用局部单调性进行 continuation/bracketing；
4. 达到可靠控制上限后切换离散路线类别；
5. 不以原始 L2 终态误差评价，而以接受集合法向误差与结果等价类评价。

### B.4 可能的 AI 载体

- 具有多个工具/编辑接口的代码代理：小而可诊断的编辑序列对比一次大范围 joint patch；警惕与 iterative refinement、unit-test localization 和 minimal patches 重合。
- 可验证推理：局部单调、错误可定位的 operator 对比高能力但反馈纠缠的 operator；警惕与 curriculum、tactic selection 和 search branching 重合。
- GPU 并行控制仿真：Brax、Isaac Gym 或其他公开连续控制基准中的 action reparameterization、robust action rank 与 feedback identifiability；警惕与 action representation、MPC、system identification 文献重合。
- 生成模型或语言模型的受约束解码：多个 token/edit 方向名义可用，但硬约束后可行流形坍缩；警惕与 constrained decoding、projection 和 verifier-guided generation 重合。

### B.5 必需证据

- 在匹配成功集合体积、模型容量和 compute 后，diagnosability 指标仍预测学习/校准速度。
- 打乱或遮蔽失败反馈会特异性消除优势。
- 只增加样本、beam width 或模型规模不能解释结果。
- 存在清晰的“自然 primitive → residual control → route switch”阶段边界。
- 指标跨至少两个机制不同的公开任务成立，否则只是某个 simulator 的调参技巧。

### B.6 最大拒稿风险

- 这是 active learning、dual control、observability、Fisher information 或 system identification 的直接翻版。
- “更容易诊断的动作更好学”过于显然。
- action manifold/viability kernel/empowerment 已覆盖有效控制维度。
- 长 primitive 序列优于耦合动作只是手工 action engineering。

## Seed C — Macro-Control beyond Point Predictability

### C.1 核心问题

在碰撞链、长时规划或模型误差使唯一终态预测失去可靠性时，智能体是否应停止优化 point prediction，转而控制宏观事件集合或结果分布？又是否存在随安全预算变化的策略相变：预算充足时选择低方差、可恢复的策略，预算不足时主动接受高方差以避免确定失败？

### C.2 反直觉主张候选

> 更差的终态点预测并不必然导致更差的决策；如果任务只依赖宏观事件，保留并校准正确的集合级预测可以在微观误差急剧增长时维持控制性能。

更具戏剧性的版本：

> 在接近确定失败的状态中，增加结果方差可以提升胜率；但只有当剩余风险预算跨过阈值时才成立。固定风险偏好的策略会在阈值两侧同时犯错。

### C.3 可能的 AI 载体

- 具有模型误差和多体交互的 GPU 物理环境，以集合级事件作为目标；必须避免论文退化为台球 simulator。
- 不完全信息或对抗性 planning benchmark，其中低预算阶段的 high-variance action 能把确定劣势转成机会；警惕与 risk-sensitive game theory、distributional RL 重合。
- Model-based RL 中随 rollout depth 自适应切换 point-state prediction 与 event/set prediction；警惕与 latent planning、value-equivalent models、temporal abstraction 重合。
- Agentic tasks 中对长程精确轨迹不可信，但可控制“是否保留可恢复状态、是否产生至少一个可行后续选项”等宏观事件；警惕与 robust planning 和 option preservation 重合。

### C.4 必需证据

- 明确测出 point prediction error 随 interaction depth 增长，而 macro-event calibration 保持稳定。
- 在相同模型容量、训练数据和 compute 下，集合级模型产生更好决策，而非仅使用更容易的目标。
- 风险预算阈值附近出现可重复的政策切换，且不是人为 reward function 直接写出的答案。
- 高方差策略只在确定劣势区间获益，在普通状态中会变差，形成可检验 phase diagram。

### C.5 最大拒稿风险

- 这是普通 distributional RL、robust MDP、risk-seeking under losses 或 value-equivalent prediction。
- 宏观标签更容易预测，因此收益没有机制新意。
- 高方差在落后时有利是经典赌博/锦标赛策略。
- 仿真环境人为设计，结论不能迁移到真实 AI 问题。

---

## 5. 暂定优先级与停止规则

| 种子 | 反直觉性 | 文献拥挤风险 | 8×4090 可行性 | 快速证伪性 | 当前建议 |
|---|---:|---:|---:|---:|---|
| A：可复位失败与认知进步 | 高 | 很高 | 高 | 高 | **第一检索优先级** |
| B：可诊断控制与可靠动作集坍缩 | 中高 | 很高 | 中高 | 中高 | **第二优先级；可能成为 A 的机制而非独立论文** |
| C：点预测失效后的宏观控制 | 高 | 极高 | 中高 | 中 | **保留为独立竞争种子，不急于合并** |

### 5.1 立即 NO-GO 条件

任一方向满足下列条件之一，应停止而不是换名字：

- 最近三年已有论文做出相同因果对照与相同反直觉结论；
- 完整 belief-state value、standard risk-sensitive objective 或 compute-matched rollout baseline 可完全解释收益；
- 正结果只来自更多重试、更多 token、更多 simulator calls 或更容易的标签；
- 只能在人工 toy environment 中出现，换两个公开 benchmark 即消失；
- 必须依赖实体机器人、超出 8×4090 的闭源模型或无法获得的数据；
- 首周无法构造冻结候选、匹配 compute 的因果对照。

### 5.2 允许进入 30 天项目的最低门槛

- 有一个精确到一句话的 residual novelty claim，而不是新术语；
- 至少一个公开自然任务和一个机制可控任务显示同一签名；
- 核心效应在两个模型规模或两类基础策略上复现；
- 消融能分别切断 reset、feedback、memory、risk budget 或 diagnosability 中的关键路径；
- 强 baseline 在 compute、反馈、候选集合和 oracle access 上公平；
- 预注册 GO/NO-GO 数值阈值，并接受干净负结果。

### 5.3 Oral 级别需要额外满足

仅有小幅性能提升不够。至少需要：

- 一个专家看前不显然、看后可解释的反直觉经验规律；
- 一个能够统一多个任务而不只是统一术语的机制；
- 一个标准评价或训练范式的明确系统性盲点；
- 一个简单方法利用该机制，并在强 baseline 上产生大而稳定的差异；
- reviewer 无法用“普通长期价值/安全探索/主动学习/分布式 RL”一句话消解。

---

## 6. 可直接交给 Pro 的英文提示词

下面的提示词是自包含的，但要求 Pro 同时完整阅读本文件和三份既有报告。建议在**原先生成 `AI_RESEARCH_REACHABILITY_EXPANSION.md` 与 `AI_RESEARCH_CARRIER_VIABILITY.md` 的同一个 Pro 对话中继续**，因为它已经掌握旧检索语境；如果旧对话上下文接近上限，则新开 Pro，并附上全部四份 Markdown。不要只粘贴摘要。

```text
You are acting as a skeptical ICLR research director, adversarial literature auditor, and falsification-first experimental designer. Your default action is to kill weak ideas, not to rescue them by renaming familiar concepts.

CURRENT DATE AND SEARCH CUTOFF
- Treat the current date as 26 August 2026.
- Search literature up to this date, with special attention to 2024–2026 papers, workshops, OpenReview submissions, arXiv preprints, official repositories, and benchmark releases.
- Prefer primary sources: official proceedings, publisher pages, OpenReview, arXiv, and official GitHub repositories. Link every important claim directly to a primary source.
- Search multiple synonymous formulations. Absence under one phrase is not evidence of novelty.

MANDATORY LOCAL INPUTS — READ ALL FOUR FILES COMPLETELY BEFORE REASONING
1. D:\ICLR_2\BILLIARDS_TO_AI_RESEARCH_SYNTHESIS.md
2. D:\ICLR_2\AI_RESEARCH_REABSTRACTION.md
3. D:\ICLR_2\AI_RESEARCH_REACHABILITY_EXPANSION.md
4. D:\ICLR_2\AI_RESEARCH_CARRIER_VIABILITY.md

The first file contains the complete new discussion and three candidate research seeds. The other three are binding negative audits. Do not rediscover or revive directions they already rejected unless you identify genuinely new evidence that changes a verdict.

HARD RESOURCE AND PROJECT CONSTRAINTS
- Exactly 8 independent NVIDIA RTX 4090 GPUs, 24 GB VRAM each.
- No NVLink and no pooled memory.
- No physical robot requirement. GPU/CPU simulation is allowed, but wall-clock time must be estimated honestly.
- Prefer open-weight models that fit one 4090 or can use ordinary data parallelism; do not assume unavailable proprietary-model training access.
- Prefer public datasets, standard benchmarks, official evaluators, strong public baselines, and reproducible code.
- The first experiment must be executable in 3–7 days. A full program should be plausible in 30 days only after explicit gates pass.
- Target venue is ICLR. The aspiration is Oral-level insight, so a predictable bias–variance curve, a renamed value function, or a small engineering gain is insufficient.

ORIGIN OF THE NEW SEEDS — DO NOT USE BILLIARDS AS NOVELTY EVIDENCE
The motivating domain produced the following observations:

1. Physical error need not shrink. A route can be better because perturbations are redirected along a task-acceptable corridor rather than across it. Raw endpoint L2 error can rank outcomes incorrectly.
2. A straight/easy current state can collapse future reliable control authority. Nominal degrees of freedom are not the same as task- and safety-constrained robust action dimensions.
3. A longer sequence of stable, natural, diagnosable primitives can be easier than one short, high-gain, coupled control action.
4. Correct discrete route class can matter more than local coordinate accuracy inside that class.
5. Microscopic outcomes of many interactions may be hard to predict, while macro-events remain controllable.
6. In defensive play, an agent may choose a route that is hard to complete because both its failure branch and success branch remain safe. It may rationally accept several small penalties rather than take an easy action whose success produces an irreversible catastrophic state.
7. After a failed attempt, the external task state is restored accurately, but the agent retains trajectory feedback and updates its internal calibration. Repeated failures are therefore not independent retries: physical state resets while epistemic state progresses.
8. Before retrying, experts pre-filter routes for downstream safety. Online adaptation then estimates contact feasibility. If a residual control variable saturates without success, they switch discrete routes.
9. Experts first use a natural, low-coupling control law, then add one residual variable, exploit local monotonicity for incremental calibration, and only then change route class.
10. Geometric tolerance alone does not determine difficulty. A narrow visual direction can be easier than a wider force interval because its error sign is observable and repeatable; channels differ in perception noise, motor noise, feedback, identifiability, and coupling.
11. When repeated safe failures consume the available risk/penalty budget, the policy can switch abruptly from low-variance resettable trials to a high-variance action that converts near-certain loss into an uncertain outcome.
12. Safe acceptance sets are joint curved regions in action space, not independent per-coordinate tolerances. Contact location and force can compensate through their effective impulse.

CANDIDATE SEEDS TO ATTACK

Seed A — Resettable Failure with Epistemic Progress
External state approximately resets after a bounded-cost failure, while internal belief/memory retains informative feedback. A lower per-attempt-success action can be globally superior because failures are safe, informative, and retryable, whereas an easier apparent success may enter an irreversible bad state. The candidate blind spot is that evaluators treating external state progress or per-attempt success as the target may label epistemically useful failure as zero or negative progress.

Seed B — Diagnosable Control under a Collapsing Robust Action Set
Task and safety constraints collapse a nominally high-dimensional action space into a low-dimensional, curved, or disconnected robust feasible set. Difficulty is not determined by set volume or dimension alone: channel-specific observability, execution noise, feedback identifiability, local monotonicity, and coupling determine finite-budget controllability. The expert pattern is natural primitive -> one residual control -> saturation test -> discrete route switch.

Seed C — Macro-Control beyond Point Predictability
As interaction depth and model mismatch grow, exact endpoint prediction may become unreliable while macro-event or set-level predictions remain calibrated and decision-useful. A risk-budget threshold may trigger a rational switch from low-variance recoverable control to high-variance actions that avoid near-certain failure.

IMPORTANT: These are competing seeds, not a preapproved unified framework. You may eliminate all three. You may merge two only if a single experiment and a single nontrivial mechanism genuinely require both. Do not manufacture a grand theory by placing known ideas under one name.

REQUIRED LITERATURE COLLISION SEARCH

For Seed A, search at minimum across:
- reversible/resettable MDPs, recoverability, safe exploration, reset policies, reversible environments;
- rollback, checkpointing, transactions, sandboxing, speculative execution, trial actions;
- learning from failure, failure-aware learning, productive failure, error-based learning, retry learning;
- active learning, Bayesian experimental design, dual control, value of information, active system identification;
- self-correction, Reflexion-style agents, verifier feedback, execution feedback, self-debugging, iterative repair;
- belief-state planning, Bayes-adaptive MDPs, meta-RL, hidden-parameter inference;
- lexicographic/constrained objectives, catastrophic success, irreversible side effects, option preservation;
- formal proving, code agents, web/GUI agents, tool agents, and planning with exact state restoration.

For Seed B, search at minimum across:
- controllability, robust controllability, viability kernels, empowerment, reachable sets;
- action-space geometry, action manifolds, low-rank control, singular controls, redundant actuation;
- observability, identifiability, Fisher information, diagnostic actions, informative actions;
- active system identification and dual control;
- continuation/homotopy, bracketing, coordinate search, residual control, gain scheduling;
- action representation learning, temporal abstraction, natural primitives, options, skill chaining;
- error-tolerant planning, anisotropic noise, sensitivity-aware planning, robust MPC;
- verifier-guided generation, code repair, proof tactics, constrained decoding, and GPU control benchmarks.

For Seed C, search at minimum across:
- distributional RL, risk-sensitive RL, robust MDP/POMDP, chance constraints;
- set prediction, event prediction, value-equivalent models, task-oriented world models;
- chaotic/sensitive dynamics under bounded model error, ensemble planning, stochastic MPC;
- outcome abstraction, macro-state prediction, causal event prediction, interaction networks;
- risk-seeking under losses, desperation strategies, tournament strategy, budgeted MDPs;
- entropy-seeking actions, randomized policies in adversarial games, minimax mixed strategies;
- adaptive prediction horizons, model exploitation, rollout-depth uncertainty, uncertainty-aware planning.

Also inspect the exact collision sets already documented in the three older reports. A paper missing only a cosmetic combination is not a novelty gap.

REQUIRED ANALYSIS

1. Reconstruct each seed in non-metaphorical language. State the strongest possible claim and the weakest trivialized version.
2. Produce a verified literature map and a novelty-collision matrix. For every close paper, state exactly what it already establishes, what experiment it runs, and whether the remaining difference is scientific or merely implementation detail.
3. Generate at least 12 mechanism-diverse AI carriers across formal reasoning, code agents, tool/web agents, generative modeling, model-based RL, adversarial decision making, and GPU simulation. Do not default to robotics. Aggressively eliminate carriers that require physical hardware, private data, excessive compute, or artificial tasks.
4. For each surviving carrier, answer:
   - What exact standard metric/evaluator/policy is predicted to fail?
   - What counterintuitive ranking inversion should occur?
   - What variable causes it?
   - What intervention would remove the effect?
   - Why is this not ordinary long-horizon value, safe exploration, active learning, dual control, or distributional RL?
5. Decide whether B is an independent paper seed, a mechanism inside A, or a NO-GO. Decide separately whether C should remain independent.
6. Select at most one primary direction and one fallback. A clean NO-GO for all seeds is acceptable and preferable to a weak recommendation.
7. For the primary direction, write formal definitions, assumptions, and 5–8 falsifiable hypotheses. At least one hypothesis must be genuinely counterintuitive and must not follow directly from the reward function by construction.
8. Design a 3–7 day killer experiment with:
   - exact public datasets/environments and official links;
   - exact open models and parameter sizes;
   - exact baselines, including the strongest obvious baseline;
   - frozen candidate sets or common-random-number comparisons where applicable;
   - compute matching in GPU-seconds, forward calls, environment calls, verifier calls, tokens, and training examples;
   - primary metrics, statistical tests, confidence intervals, seeds, and effect-size thresholds;
   - causal ablations for reset, retained feedback, memory, diagnosability, residual-control saturation, and risk budget as relevant;
   - explicit GO, NO-GO, and ambiguous-outcome rules by Day 2, Day 4, and Day 7;
   - honest wall-clock and GPU-hour estimates for 8x4090.
9. If and only if the killer experiment has a plausible positive regime, give a gated 30-day plan. Do not recommend architecture building before the phenomenon is verified.
10. Write the strongest skeptical ICLR rejection paragraph and the exact evidence needed to defeat it.
11. Estimate the probability of: synthetic effect, natural-task transfer, ICLR main-track quality, and Oral-level quality. These must be calibrated judgments, not promotional numbers.
12. End with a binding cluster decision: DO NOT RUN, 2-GPU PILOT, 1-WEEK 8-GPU SPRINT, or CONDITIONAL 30-DAY PROGRAM.

NON-NEGOTIABLE NOVELTY RULES
- Do not treat a new name, metric, or unified notation as a contribution.
- Do not claim novelty because no paper uses the billiards analogy.
- Do not call a result surprising if it is directly encoded in the reward function.
- Do not accept “more retries help,” “feedback helps self-correction,” “rollback prevents damage,” “uncertainty grows with horizon,” “macro labels are easier,” “more actions can make search harder,” or “risk-seeking can help when losing” as sufficient contributions.
- Do not rescue an occupied broad idea by narrowing to a benchmark-specific engineering trick.
- A missing combination of known components is insufficient unless the combination produces a new, causal, and externally useful empirical law.

OUTPUT CONTRACT
- Produce one self-contained English Markdown document.
- Suggested filename: D:\ICLR_2\AI_RESEARCH_RESET_DIAGNOSTICITY_AUDIT.md
- The document must be understandable without the billiards story, although one short motivation paragraph is allowed.
- Include an executive verdict at the top, direct primary-source links near every literature claim, a collision matrix, elimination funnel, formal hypotheses, killer experiment, compute ledger, reviewer attacks, and binding GO/NO-GO thresholds.
- Clearly label verified facts, literature-supported judgments, inferences, hypotheses, and project decisions.
- Do not output a chatty preface. The final response should be the complete Markdown artifact only.
```

---

## 7. 交付前自审

### 7.1 贡献与范围

- **通过：** 文档没有宣称三个种子已具备创新性。
- **通过：** 旧报告的 NO-GO 结论被设置为硬约束。
- **待证据：** Seed A 是否超越 active learning、self-correction、rollback 和 belief-state planning。
- **待证据：** Seed B 是否有超出 observability/dual control/action representation 的残余。
- **待证据：** Seed C 是否能超越 distributional/risk-sensitive RL 的标准结论。

### 7.2 机制完整性

- **通过：** 已保留误差走廊、非点状好球区、可靠可达性、自然多库、加塞、K 球、防守、复位校准、风险预算、控制维度坍缩、通道可诊断性和联合接受集合。
- **通过：** 已区分物理误差缩小、任务误差投影、理论可达与可靠可达。
- **通过：** 已明确“高方差脱困”主要是被迫接受随机性，而不是可以精确设计所有随机结果。

### 7.3 实验与可执行性

- **尚未通过：** 当前没有被授权的具体 benchmark、模型或实验脚本。
- **下一门：** Pro 必须先给出 primary-source 文献碰撞与 3–7 天杀手实验。
- **资源纪律：** 在 Day-2 机制分离之前，不应占用完整 8 卡搭建大型系统。

### 7.4 最强预期拒稿意见

> The submission combines resettable exploration, learning from failure, diagnostic action selection, and risk-sensitive control under a new vocabulary. Every component is already expressible in a Bayes-adaptive belief-state MDP and is well studied in active learning, dual control, safe exploration, rollback-enabled agents, and distributional reinforcement learning. The billiards motivation is intuitive but supplies no new scientific object. The experiments merely show that informative retries help when the environment is reset and that high variance can help under near-certain loss—both conclusions are expected from the constructed objective.

任何后续报告如果不能用具体文献空隙、因果对照和自然任务上的反常结果击败这段拒稿意见，就应判定 NO-GO。

### 7.5 主要主张—证据状态表

| 主要主张 | 当前依据 | 状态 |
|---|---|---|
| 误差沿接受集合切向传播可优于更小的原始 L2 误差 | 台球走位几何与镜像解释 | **机制合理；AI 证据缺失** |
| 可复位失败能够同时保持外部安全并积累认知进步 | 斯诺克复位解球经验 | **核心假设；必须在自然 AI 任务中验证** |
| 标准 evaluator 会系统性低估这种失败 | 尚无直接实验 | **最关键待证主张** |
| 动作容差体积不足以预测校准难度，可诊断性提供额外解释 | 方向与力度通道差异 | **待文献审计与对照实验** |
| 微观点预测失效时宏观事件仍可控制 | K 球经验与现实模型不确定性 | **有物理动机；AI 决策收益待证** |
| 风险预算会触发低方差到高方差的政策相变 | 连续罚分后的大力解球策略 | **经验假设；极易撞 risk-sensitive 文献** |
| 三个机制应统一成一个框架 | 当前没有证据 | **不支持；禁止预先合并** |
