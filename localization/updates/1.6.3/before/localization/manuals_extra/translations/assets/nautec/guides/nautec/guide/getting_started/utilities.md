---
navigation:
  title: 工具与实用功能
  icon: nautec:aquarine_steel_wrench
  position: 7
  parent: getting_started/getting_started-index.md
item_ids:
  - nautec:aquarine_steel_wrench
  - nautec:configuration_card
---

# <Color id="light_purple">工具与实用功能</Color>

<Column alignItems="center" fullWidth={true}>
  <ItemImage id="aquarine_steel_wrench" scale="2"/>
  扳手用于设置和旋转 海蓝科技 方块, 并设置机器的哪些面可供漏斗和管道使用.
</Column>

***

<Row>
  <ItemImage id="aquarine_steel_wrench"/>
  ### <Color id="aqua">海蓝钢扳手</Color>
</Row>

扳手有四种模式. 潜行并右键点击空气可在它们之间切换; 提示框和快捷栏上方的消息会显示当前模式.

* 旋转: 右键点击任何有朝向的方块, 例如<ItemLink id="aquatic_catalyst"/>, 中继器或机器, 可将其转向下一个方向. 继续点击可转完一整圈.
* 物品面和流体面: 右键点击机器的某个面可改变漏斗和管道通过该面能做什么, 潜行右键点击则回退. 在物品面模式下, 已成型生物反应机或工业生物反应机的任何方块都会设置整个反应机的该侧. 见下方的侧面配置.
* 连接: 点击两次即可让两个激光方块互相对准. 先右击发射光束的方块, 例如<ItemLink id="prismarine_laser_relay"/>, <ItemLink id="laser_junction"/>或<ItemLink id="aquatic_catalyst"/>, 将其存为起点. 再右击光束要到达的方块, 例如另一个中继器或机器. 扳手会转动起点, 让它朝第二个方块发射, 并转动第二个方块以接收起点的光束; 对转接器则改为开启对应的输出面或输入面. 两个方块必须在同一直线上, 且在光束射程内. 如有障碍物, 快捷栏上方会显示提示. 连接后保存的起点会清空, 可以继续下一次连接. 右击空气或不收发激光的方块也会清空起点; 已保存起点时, 提示框会显示其位置. 此模式操作机器时不会打开界面. 中继器从背面接收光束, 从正面发射, 因此将其向拐角后的下一处连接会使其转离原本接收的光束; 此时会显示警告. 需要转弯时应使用<ItemLink id="laser_junction"/>.

以下操作在所有模式下都有效:

* 未成型的强化站, 生物反应机, 工业生物反应机或深海排水口, 在不潜行时点击其控制器方块即可成型.
* 点击<ItemLink id="gateway"/>会使其形成环, 对已形成的环潜行右键点击可将整个环收进一个物品. 参见[传送门](nautec:deep_engineering/gateway.md).
* 对自己培育的海棱水晶潜行右键点击可拾起整株水晶. 野生水晶无法移动. 参见[水晶培育](nautec:deep_engineering/crystal_cultivation.md).
* 右键点击海洋侦察艇会打开其模块界面. 参见[海洋侦察艇](nautec:submarine/submarine.md).
* 右键点击<ItemLink id="laser_junction"/>的某个面会使其成为输入, 潜行右键点击则成为输出. 以相同方式再次点击该面会将其关闭.
* 已成型[生物反应机](nautec:aquatic_biology/bio_reactor.md)顶部的边缘方块, 已成型[工业生物反应机](nautec:aquatic_biology/industrial_bio_reactor.md)的顶部方块, 或已成型[深海排水口](nautec:laser_chemistry/drain.md)中层墙壁方块的外侧面, 会在该处开启一个激光端口, 使光束可以为机器供能. 对于排水口, 端口就是你点击的那个面, 因此请点击侧面, 而不是顶部或底部. 反应机的端口再次点击会关闭. 在反应机上, 此操作在物品面模式下无效, 因为该模式设置的是反应机的侧面.

<Recipe id="nautec:aquarine_wrench"/>

***

## <Color id="gold">侧面配置</Color>

每台容纳物品或流体的 海蓝科技 机器都允许你逐面选择自动化在那里能做什么. 物品和流体分别设置. 每个面有四种模式之一:

* 输入和输出(绿色): 漏斗和管道可插入输入槽, 并从输出槽抽取. 每个面最初都是这样.
* 插入(蓝色): 漏斗和管道可插入, 但不会有东西出来.
* 抽取(橙色): 漏斗和管道可抽取, 但不会有东西进去.
* 关闭(灰色): 漏斗和管道完全无法访问此面.

无论面模式如何, 机器只会将输入放入输入槽, 并从输出槽给出输出, 因此管道无法把你的原料抽回去.

可用处于物品面或流体面模式的扳手改变某个面, 或打开机器并点击其界面右边缘的小标签. 该标签会打开一个六面十字: 前, 后, 左, 右, 顶和底, 以你面向机器正面时的方向命名. 左键点击某个面切换到下一模式, 右键点击则切换到上一模式. 同时容纳物品和流体的机器在面的上方有物品和流体按钮. 没有朝向, 或朝向正上或正下的机器, 以北面作为正面.

生物反应机和工业生物反应机为整个结构每侧只有一个物品设置: 反应机界面中的面代表多方块的六个外侧面, 其北面为正面. 其他多方块结构, 例如深海排水口和聚变电站, 保留各自的规则, 在其页面上说明.

***

<Row>
  <ItemImage id="configuration_card"/>
  ### <Color id="aqua">配置卡</Color>
</Row>

将设置从一个方块复制到另一个方块. 潜行右键点击机器可将其设置复制到卡上, 然后右键点击另一个方块进行粘贴. 潜行右键点击空气可清空配置卡. 提示框会显示设置的来源及其覆盖范围. 手持配置卡右键点击始终会粘贴, 即使该方块本来会打开其界面.

* 侧面配置可粘贴到任何具有侧面配置的机器上, 因此一张卡可以用相同方式设置一整排不同的机器.
* 方块自身的设置只会粘贴到同种方块上:
  * <ItemLink id="confined_spawner"/>的过滤器和白名单模式
  * <ItemLink id="resonance_node"/>的网络, 输入或输出模式, 优先级, 限制和区块加载
  * <ItemLink id="uplink_array"/>的网络和区块加载
  * <ItemLink id="laser_junction"/>的输入和输出面
  * 导管接口的面
  * <ItemLink id="laser_purification_smelter"/>的自动分配设置
* 升级和过滤器也会复制, 同样只限于同种方块: 导管接口的升级和过滤器, <ItemLink id="energy_converter"/>的升级, 生物反应机的升级, 以及激光提纯熔炉的导管升级. 粘贴时会从你的物品栏中取出它们, 并返还目标方块在这些槽位中原有的东西. 如果你缺少其中任何一个, 则不会粘贴任何内容, 配置卡会告诉你需要什么.

粘贴共鸣网络时会检查你是否被允许使用它, 与在界面中选择它相同.

<Recipe id="nautec:configuration_card"/>
