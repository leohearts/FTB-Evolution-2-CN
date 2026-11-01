---
navigation:
  title: 约束刷怪笼
  icon: nautec:spawner_confinement_matrix
  position: 12
  parent: laser_chemistry/laser_chemistry-index.md
item_ids:
  - nautec:spawner_confinement_matrix
  - nautec:confined_spawner
  - nautec:mob_sampler
  - nautec:mob_sample
---

# <Color id="light_purple">约束刷怪笼</Color>

<Column alignItems="center" fullWidth={true}>
  <ItemImage id="spawner_confinement_matrix" scale="2"/>
  把刷怪笼变成一台直接将生物掉落物存入自身存储的机器, 完全不生成任何生物.
</Column>

## <Color id="gold">对刷怪笼进行约束</Color>

对刷怪笼使用刷怪笼约束矩阵. 笼子会多出一圈发光的符文和金属框架, 变成约束刷怪笼. 它会保留原刷怪笼的一切: 生物种类, 单次生成数量, 生成频率以及所有升级. 用 Apothic Spawners 强化过的刷怪笼会保留其生成数量和延迟, 并因此运行得更快.

潜行并用空手或刷怪笼约束矩阵对约束刷怪笼使用, 可将其释放. 笼子会恢复为普通刷怪笼, 并保留当前的生物和升级, 刷怪笼约束矩阵会回到你的物品栏. 只有当存储和经验储罐都为空时才能释放; 在此之前会提示先清空它们.

用镐破坏约束刷怪笼会掉落约束刷怪笼本身, 无论是否使用精准采集. 它会保留生物, 刷怪笼的设置和升级以及过滤器, 因此你可以搬运它并原样放回. 存储的掉落物和经验也会一同保留, 不会有东西洒到地上. 若想取回普通刷怪笼, 请清空它然后释放.

## <Color id="gold">更换生物</Color>

在搅拌机中用一个玻璃试管, 两个海蓝铜锭, 一颗钻石和 250 mB 电解藻类浆液制作<ItemLink id="mob_sampler"/>. 每次配方产出一个采样器.

对活着的生物使用采样器即可采集<ItemLink id="mob_sample"/>. 该生物会存活并留在原地. 采样器会被消耗, 样本的提示信息会注明其来源生物. 其他模组添加的生物同样适用.

对约束刷怪笼使用样本可更换其生物. 样本会被消耗. 生成数量, 延迟, 升级, 过滤器, 存储的掉落物和经验都会保留; 下一周期的进度会重新开始. 破坏并重新放置刷怪笼会保留新生物, 释放回普通刷怪笼时也是如此. 样本不能直接用于普通刷怪笼.

玩家, 已死亡的生物以及带有 `c:capturing_not_supported` 实体类型标签的实体无法采样. 使用样本时会再次检查该标签, 因此整合包也可以阻止在规则更改前采集的样本.

<RecipeFor id="mob_sampler"/>

### <Color id="aqua">守卫者材料</Color>

守卫者是很适合首先采样的目标. 守卫者约束刷怪笼可再生地提供海晶碎片和海晶砂粒, 用于[海蓝催化器燃料](nautec:getting_started/laser_power.md)和 海蓝科技合成, 包括海蓝铜混合物.

它还有几率产出<ItemLink id="ancient_valve"/>, <ItemLink id="burnt_coil"/>和<ItemLink id="guardian_eye"/>. 这能为你自动供应打捞零件和守卫者之眼, 用于增强模块和脉冲激光模块. 额外的生物掉落参见[打捞](nautec:getting_started/salvage.md), 清理打捞零件参见[板条箱与蚀刻](nautec:getting_started/etching.md).

## <Color id="gold">能量</Color>

将激光束对准任意一面. 刷怪笼最多储存 500 AP, 运行时每 tick 消耗 50 AP, 因此 50 AP 或更强的光束可让它不间断运行. 更弱的光束也能用, 但会在缓冲区重新填满时间歇运行. 供应方式参见[激光能量](nautec:getting_started/laser_power.md).

只要它有能量且存储中还有空位就会运行, 不需要附近有玩家, 也不受光照或空间规则限制. 工作时符文会变亮, 里面的生物会转得更快.

## <Color id="gold">掉落物</Color>

每个周期耗时与原刷怪笼自身的生成延迟相同. 周期结束时, 刷怪笼会按原本会生成的生物数量各掷一次生物战利品, 并按玩家击杀计算, 因此需要玩家击杀的掉落物也会包含在内. 结果会存入 54 个存储槽位, 与一个双箱子相同.

当所有槽位都被占用时, 刷怪笼会暂停, 并让缓冲区保持充满, 直到有槽位空出. 某次掷取中放不下的部分会丢失.

漏斗和管道可以抽出掉落物, 默认从任意一面([侧面配置](nautec:getting_started/utilities.md)). 只有刷怪笼本身会放入物品.

## <Color id="gold">经验</Color>

刷怪笼还会保留生物本应掉落的经验, 以液态经验形式储存在容量为 16,000 mB 的储罐中. 每点经验转化为 20 mB, 这是大多数模组用于液态经验的比率. 储罐装满后, 新的经验会丢失; 刷怪笼会继续运行.

默认情况下该液体是经验藻液, 一种发光的绿色流体. 如果你的整合包有其他模组的液态经验, 可在 `config/nautec-common.toml` 的 `confinedSpawnerXpFluids` 中将其流体 id 列在最前面, 刷怪笼就会改为生产该液体. 经验藻液位于 `c:experience` 流体标签中, 因此按标签接受液态经验的模组也能接受它.

可以用管道从任意一面抽出经验(流体与物品分开遵循[侧面配置](nautec:getting_started/utilities.md)), 或用空桶右键点击刷怪笼. 管道只能抽取储罐. 界面左侧标签的第三条显示其装满程度. 破坏刷怪笼时经验会保留在掉落的物品中.

## <Color id="gold">界面</Color>

右键点击刷怪笼可查看其存储并取出物品. 左侧标签有三条进度条: 储存的 AP, 当前周期的进度以及液态经验. 将鼠标悬停在进度条上可查看数值. 未运行时, 标题旁的状态会说明停止的原因.

## <Color id="gold">过滤掉落物</Color>

标题旁的漏斗按钮会打开过滤面板, 其中有 18 个过滤槽位.

* 手持物品点击某个槽位可过滤该物品. 也可以从 JEI 拖入物品.
* 右键点击已填充的槽位可在该物品的标签之间切换, 然后回到精确物品. 标签过滤会匹配该标签中的每个物品, 并显示金色的 **#**.
* 用空手点击槽位可清空它.

顶部的按钮在两种模式之间切换:

* **黑名单**会产出除已过滤掉落物之外的一切.
* **白名单**只产出已过滤的掉落物.

已过滤的掉落物永远不会产出, 因此不会占用存储. 空的白名单会让刷怪笼停止, 直到你添加过滤器.

## <Color id="gold">Jade</Color>

安装 Jade 后注视约束刷怪笼, 会显示其生物, 是否正在运行, 储存的 AP 以及存储中的内容.

***

### <Color id="aqua">刷怪笼约束矩阵配方</Color>

<RecipeFor id="spawner_confinement_matrix"/>
