---
navigation:
  title: 合成强化
  icon: nautec:magnetic_coil_arm
  position: 4
  parent: laser_augmentation/laser_augmentation-index.md
item_ids:
  - nautec:hydraulic_leg
  - nautec:servo_knee
  - nautec:shock_absorber
  - nautec:tendon_weave
  - nautec:magnetic_coil_arm
  - nautec:ender_coil_arm
  - nautec:hydro_drill_arm
  - nautec:syringe_robot_arm
  - nautec:trident_launcher_arm
  - nautec:volley_trident_arm
  - nautec:buoyancy_tank
  - nautec:auxiliary_ventricle
---

# <Color id="light_purple">合成强化</Color>

<Column alignItems="center" fullWidth={true}>
  <ItemImage id="magnetic_coil_arm" scale="2"/>
  有十二种强化部件在合成台中制作, 而不是由生物掉落.
</Column>

每个部件都像其他部件一样在[强化站](augmentation_station.md)安装.

***

## <Color id="gold">腿部</Color>

四个部件会争夺左腿和右腿槽位.

<Row>
  <ItemImage id="hydraulic_leg"/>
  ### <Color id="aqua">液压腿</Color>
</Row>

强化: 跳跃. 站在地面上时按左 Alt, 你会朝视线方向弹射出去. 垂直向上看即可向上跳跃. 冷却时间略长于一秒.

<Recipe id="nautec:hydraulic_leg"/>

<Row>
  <ItemImage id="servo_knee"/>
  ### <Color id="aqua">伺服膝关节</Color>
</Row>

强化: 自动上台阶. 你可以不用跳跃就走上整格高的方块.

<Recipe id="nautec:servo_knee"/>

<Row>
  <ItemImage id="shock_absorber"/>
  ### <Color id="aqua">减震器</Color>
</Row>

强化: 免疫摔落伤害. 从任何高度摔落都不会受到伤害. 它与液压腿搭配良好.

<Recipe id="nautec:shock_absorber"/>

<Row>
  <ItemImage id="tendon_weave"/>
  ### <Color id="aqua">肌腱编织物</Color>
</Row>

强化: 行走速度. 将你的基础行走速度提高到正常速度的两倍半.

<Recipe id="nautec:tendon_weave"/>

***

## <Color id="gold">功能手臂</Color>

六个部件会争夺左臂和右臂槽位. 以下三个会自行生效.

<Row>
  <ItemImage id="magnetic_coil_arm"/>
  ### <Color id="aqua">磁力线圈臂</Color>
</Row>

强化: 磁力. 将 5 格范围内的掉落物拉向你. 潜行可将其关闭, 例如当你想丢弃物品时.

<Recipe id="nautec:magnetic_coil_arm"/>

<Row>
  <ItemImage id="ender_coil_arm"/>
  ### <Color id="aqua">末影线圈臂</Color>
</Row>

强化: 末影磁力. 将 5 格范围内的掉落物直接传送到你的物品栏. 放不下的物品会留在原处. 潜行可将其关闭.

<Recipe id="nautec:ender_coil_arm"/>

<Row>
  <ItemImage id="hydro_drill_arm"/>
  ### <Color id="aqua">水力钻臂</Color>
</Row>

强化: 水下挖掘速度. 消除头部浸入水中时的挖掘减速, 效果等同于不戴头盔的水下速掘. 漂浮时挖掘仍然缓慢, 所以请站在底部.

<Recipe id="nautec:hydro_drill_arm"/>

***

## <Color id="gold">投掷手臂</Color>

这三个部件通过按键发射, 冷却时间均为一秒. 它们不消耗弹药, 投出的东西也无法拾取.

<Row>
  <ItemImage id="trident_launcher_arm"/>
  ### <Color id="aqua">三叉戟发射臂</Color>
</Row>

强化: 弹射三叉戟, 按键 Y. 投出一把三叉戟, 它会在击中第一个方块时反弹一次并继续飞行. 命中生物会结束反弹.

<Recipe id="nautec:trident_launcher_arm"/>

<Row>
  <ItemImage id="volley_trident_arm"/>
  ### <Color id="aqua">三叉戟齐射臂</Color>
</Row>

强化: 散射三叉戟, 按键 U. 投出一把三叉戟, 命中方块时会分裂成三把, 从命中点呈扇形散开. 对准生物群附近的地面或墙壁投掷.

<Recipe id="nautec:volley_trident_arm"/>

<Row>
  <ItemImage id="syringe_robot_arm"/>
  ### <Color id="aqua">注射器机械臂</Color>
</Row>

强化: 随机投掷药水, 按键 G. 投出一瓶随机选择的喷溅药水, 可能为治疗, 伤害, 生命恢复, 迅捷或缓慢. 五种中有两种会伤害或减速命中的目标, 所以不要朝自己脚下投掷.

<Recipe id="nautec:syringe_robot_arm"/>

***

## <Color id="gold">身体与心脏</Color>

<Row>
  <ItemImage id="buoyancy_tank"/>
  ### <Color id="aqua">浮力罐</Color>
</Row>

强化: 创造飞行, 位于身体槽位. 你可以像创造模式那样飞行: 双击跳跃起飞, 在水中或水外均可. 它占用身体槽位, 因此会替换海豚鳍或发光皮肤.

<Recipe id="nautec:buoyancy_tank"/>

<Row>
  <ItemImage id="auxiliary_ventricle"/>
  ### <Color id="aqua">辅助心室</Color>
</Row>

强化: 额外生命, 位于心脏槽位. 使你的最大生命值翻倍, 从 10 颗心提升到 20 颗. 它与 <ItemLink id="eldritch_heart"/> 强化共用心脏槽位, 因此你需要在更多生命与水中治疗之间做出选择.

<Recipe id="nautec:auxiliary_ventricle"/>
