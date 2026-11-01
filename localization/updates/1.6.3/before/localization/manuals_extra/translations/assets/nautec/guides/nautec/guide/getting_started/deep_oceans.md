---
navigation:
  title: 深海海洋
  icon: nautec:luminescent_algae
  position: 11
  parent: getting_started/getting_started-index.md
item_ids:
  - nautec:hydrothermal_vent
---

# <Color id="light_purple">深海海洋</Color>

<Column alignItems="center" fullWidth={true}>
  <ItemImage id="luminescent_algae" scale="2"/>
  海蓝科技 新增了四个海洋生物群系, 每个都拥有自己的植物和生物.
</Column>

这四个生物群系是附加在原版海洋之上的, 并不会替换它们. 它们只会在尚未生成的区块中生成, 因此在已有世界中, 你会在已探索区域边缘之外找到它们.

这四个生物群系都算作海洋. [深海排水口](nautec:laser_chemistry/drain.md), 幸运钓鱼区, 海蓝科技 结构, 原版海底废墟和沉船在其中都能正常工作, 当整合包在 `config/nautec-common.toml` 中开启 `collectSaltWater` 时, 用桶采集盐水也同样有效.

海蓝科技 还会让海洋比原版更深. 安装 Tectonic 后, 海洋深度改由 Tectonic 决定.

| 生物群系 | 位置 | 能见度 |
|---|---|---|
| 深渊海沟 | 离陆地最远, 寒冷气候 | 约 20 格 |
| 荧光海林 | 深海, 温带气候 | 约 130 格 |
| 海底热泉 | 深海, 温暖气候 | 约 50 格 |
| 海晶礁 | 海岸附近的浅水, 温带到炎热气候 | 约 145 格 |

***

## <Color id="gold">深渊海沟</Color>

四个生物群系中最深, 最暗的一个, 水色近乎漆黑, 还有漂浮的微粒.

* 溺尸的生成频率远高于其他海洋, 深渊巨口会在 Y 40 以下的黑暗中捕猎.
* 深渊珊瑚生长在海底. 淤泥跳鱼, 鳕鱼, 鱿鱼和发光鱿鱼在这里游动.
* <ItemLink id="budding_prismarine"/>生成在海床顶部. 留意它发出的微光.
* 这里是[深海压力锻炉](nautec:deep_engineering/pressure_forge.md)的最佳位置, 它需要足够的深度以及上方的一柱水体.

***

## <Color id="gold">荧光海林</Color>

清澈的青绿色水体, 其中有发光的孢子漂浮.

* 海底生长着深海海带, 荧光藻, 海草和海泡菜, 荧光珊瑚虫则会在海底, 墙壁和天花板的石头上蔓延.
* 灯笼水母, 淤泥跳鱼以及额外的发光鱿鱼.
* 海晶母岩与海沟中一样, 生成在海床顶部.

### 荧光洞窟

荧光海林海底下方被掏空形成的充水洞穴, 需要从海床沿狭窄的竖井向下到达. 荧光珊瑚虫覆盖墙壁, 荧光藻和海泡菜照亮底部, 因此从竖井中就能发现它们.

* 每个洞窟的底部都有一个<ItemLink id="budding_prismarine"/>, 通常还已经长出了海晶簇.
* 大约三分之一的洞窟底部有一个<ItemLink id="rusty_crate"/>, 里面装有打捞物.
* 它们绝不会通向干燥的洞穴, 因此洞窟中总是充满水.

***

## <Color id="gold">海底热泉</Color>

浑浊的褐色水体, 海底散布着玄武岩和岩浆, 气泡不断升起.

* 热泉管虫生长在海底.
* 热泉爬行者在海底行走, 并掉落甲壳板.
* 海底裸露的岩浆会形成气泡柱, 可用玻璃瓶装入压缩空气, 供[潜水服](diving_gear.md)使用.

### 热泉区

由两到五座玄武岩和黑石构成的黑色烟囱从海底升起, 最高的可达八格. 每座顶部都有一个<ItemLink id="hydrothermal_vent"/>, 不断喷出烟雾和气泡, 其内部和下方有岩浆, 底部周围聚集着热泉管虫.

* 烟囱壁上散布着铜, 铁和金矿石.
* 海底热泉口会像岩浆一样灼烧站在上面的任何东西. 潜行即可安全通过.
* 用镐挖掘即可将其带回家. 放在它上方的[热泉汲取器](nautec:getting_started/ocean_generators.md)会把它算作三种热源, 相当于三个岩浆块.

***

## <Color id="gold">海晶礁</Color>

明亮清澈的浅水.

* 海底有珊瑚, 海泡菜和成片的海晶石, 其间生长着海晶叶丛.
* <ItemLink id="budding_prismarine"/>位于海底顶部和海晶石斑块中. 这里是最容易找到它的地方.
* 热带鱼, 淤泥跳鱼, 鱿鱼和海豚.

***

## <Color id="gold">供整合包作者参考</Color>

`config/nautec-worldgen.toml` 中的 `enableBiomeInjection` 可以关闭这些生物群系. 使用自定义主世界预设的整合包应将其加入 `injectableWorldPresets`. 安装 Lithostitched 后, 生成位置改由 `data/nautec/lithostitched/biome_injector` 中的生物群系注入器文件决定, 这也涵盖 Terralith 和 Tectonic.

生物群系标签 `nautec:has_budding_prismarine` 列出了海床中会偶尔生成海晶母岩的非 海蓝科技 生物群系, 默认是暖水海洋和深暖水海洋. 把其他模组的暖水海洋加入其中, 就能让它们也获得同样的效果. `nautec:budding_prismarine_grafting` 列出了可以从海晶母岩移植嗜岩石菌的生物群系, 并且已经包含第一个标签.

植物和生物见[深海生命](deep_life.md).
