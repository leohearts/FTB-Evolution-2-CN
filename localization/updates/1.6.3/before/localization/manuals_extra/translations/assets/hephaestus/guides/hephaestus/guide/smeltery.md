---
navigation:
  parent: index.md
  title: 冶炼炉
  position: 10
  icon: hephaestus:smeltery_controller
item_ids:
  - hephaestus:smeltery_controller
---

# 冶炼炉

冶炼炉是一种多方块熔炉.它可以将矿石和金属熔化成液体, 一次处理多种材料, 排液口可让你将产物浇铸到铸型中.

<GameScene zoom="4" interactive={true}>
  <ImportStructure src="smeltery.nbt" />
  <IsometricCamera yaw="225" pitch="30" />

  <BoxAnnotation min="1.97 0.97 0.97" max="3.03 2.03 2.03" color="#ffd83a" thickness="0.06" alwaysOnTop={true}>
    **冶炼炉控制器**. 朝外, 背对内部.
  </BoxAnnotation>

  <BoxAnnotation min="0.97 0.97 0.97" max="2.03 2.03 2.03" color="#ff7043" thickness="0.06" alwaysOnTop={true}>
    **焦黑燃料罐**. 装入熔岩.
  </BoxAnnotation>

  <BoxAnnotation min="2.97 0.97 0.97" max="4.03 2.03 2.03" color="#4fc3f7" thickness="0.06" alwaysOnTop={true}>
    **焦黑排液口**. 朝外.在上面放一个焦黑浇口以进行浇铸.
  </BoxAnnotation>

  <BoxAnnotation min="2.97 0.97 -0.03" max="4.03 2.03 1.03" color="#81c784" thickness="0.06" alwaysOnTop={true}>
    **焦黑浇口**. 安装在排液口正面.右击它以浇铸.
  </BoxAnnotation>

  <BoxAnnotation min="2.97 -0.03 -0.03" max="4.03 1.03 1.03" color="#ce93d8" thickness="0.06" alwaysOnTop={true}>
    **焦黑铸件台**. 位于浇口下方, 承接金属.
  </BoxAnnotation>
</GameScene>

此示例有一个 3x3 的内部和一层炉壁: 9 个底部方块和 12 个炉壁方块, 共 21 个.前方的浇口和铸件台不属于冶炼炉, 但它们是取出金属的方式.拖动场景可以旋转视角.

## 形状

- **底部:** 内部每个方块下方各有一个焦黑方块.底部不会延伸到炉壁下方.
- **炉壁:** 围绕内部的一圈方块, 与内部同高, 因此比底部高一格.四个角留空, 因为冶炼炉从不检查它们.
- **内部:** 只能是空气或液体, 沿控制器所在炉壁方向宽 1x1 至 15 格, 远离该壁的深度为 8 格.冶炼炉从控制器后方的方块开始测量, 每侧最多 7 格, 因此要把控制器放在炉壁中央才能获得完整宽度.
- **高度:** 在上方叠加更多环以增加高度, 最多 64 层.每一层都必须是**完整**的环, 否则冶炼炉根本无法成型.

## 组件

- <ItemImage id="hephaestus:smeltery_controller" scale="0.5" /> **冶炼炉控制器**: 安装在炉壁中, 不能放在角落, 朝外.其后方方块必须是内部的一部分.
- <ItemImage id="hephaestus:seared_fuel_tank" scale="0.5" /> **焦黑燃料罐**: 可安装在炉壁的任意位置.冶炼炉会消耗其中的燃料.熔岩可用, JEI 会显示更坚韧的金属所需的温度更高的燃料.
- <ItemImage id="hephaestus:seared_drain" scale="0.5" /> **焦黑排液口**: 可安装在炉壁的任意位置, 朝外.熔融金属从中流出.

## 浇铸

- <ItemImage id="hephaestus:seared_faucet" scale="0.5" /> **焦黑浇口**: 放置在排液口的外侧面.它从后方方块抽取, 并浇铸到下方方块中.
- <ItemImage id="hephaestus:seared_table" scale="0.5" /> **焦黑铸件台**: 放置在浇口正下方.右击浇口进行浇铸.

## 允许的方块

- **底部:** 任意焦黑石或焦黑砖方块, 例如<ItemImage id="hephaestus:seared_bricks" scale="0.5" /> **焦黑砖块**或<ItemImage id="hephaestus:seared_stone" scale="0.5" /> **焦黑石**.
- **炉壁:** 任意底部方块, 外加<ItemImage id="hephaestus:seared_glass" scale="0.5" /> **焦黑玻璃**, <ItemImage id="hephaestus:clear_glass" scale="0.5" /> **透明玻璃**, <ItemImage id="hephaestus:seared_chute" scale="0.5" /> **焦黑滑槽**, <ItemImage id="hephaestus:seared_ladder" scale="0.5" /> **焦黑梯子**, 燃料罐, 以及上述三种组件.

## 尺寸

能成型的最小冶炼炉有一个 1x1 的内部: 1 个底部方块和 4 个炉壁方块 (控制器, 排液口, 燃料罐和一块焦黑砖), 因此共 **5 个方块**.

内部的每个方块可容纳 **1 个物品**和 **8,000 mB** 液体.上方的 3x3 示例一次可熔化 9 个物品, 并可容纳 72,000 mB.
