---
navigation:
  title: 内燃发电机
  icon: nautec:combustion_dynamo
  position: 16
  parent: getting_started/getting_started-index.md
item_ids:
  - nautec:combustion_dynamo
  - nautec:kelp_slurry
  - nautec:algal_lipid
---

# <Color id="light_purple">内燃发电机</Color>

<Column alignItems="center" fullWidth={true}>
  <Row>
    <ItemImage id="combustion_dynamo" scale="2"/>
  </Row>
  一台燃烧原油和水来产生 Forge 能量(FE)的引擎.
</Column>

内燃发电机在有原油和水时产生 320 FE/t, 并将其输送到任何接触它的电缆或机器中. 原油来自一种把海带转化为脂质的菌株, 因此一个海带农场和一台生物反应机就能让它永久运行.

***

## <Color id="gold">运行</Color>

* **原油.** `c:oil` 标签中的任何原油都可用, 包括 海蓝科技 自有的和其他模组的. 它每 10 tick 燃烧 1 mB, 因此一桶可燃烧超过 8 分钟.
* **水.** 它还会每 tick 消耗 1 mB 水, 即每秒 20 mB.
* **储罐.** 它分别为两种流体配有独立的 8,000 mB 储罐. 把两种流体从任意一面输入: 原油只会进入原油罐, 水只会进入水罐, 因此一根管道可以同时输送两者.
* **添加剂.** 在槽位中放入红石可把产出提高到 480 FE/t. 一份红石可维持一分钟的燃烧, 并在持续期间让引擎多消耗 10% 的原油和水. 计时只在引擎燃烧时进行.

界面会显示产出, 引擎缺少什么以及剩余增幅时间. Jade 会从外部显示同样的信息.

***

## <Color id="gold">制造原油</Color>

<Row>
  <ItemImage id="kelp_slurry"/>
  ### <Color id="aqua">海带浆</Color>
</Row>

在[搅拌机](nautec:laser_chemistry/mixer.md)中把 4 个海带与 1,000 mB 盐水混合, 制成 2 个海带浆.

<Row>
  <ItemImage id="algal_lipid"/>
  ### <Color id="aqua">嗜脂菌与藻类脂质</Color>
</Row>

嗜脂菌是一种能产生藻类脂质的菌株. 在[诱变机](nautec:aquatic_biology/mutator.md)中以海带浆为催化剂, 从盐养菌诱变得到(每次尝试 10%), 然后像其他菌株一样用海带浆培养并喂养它们. [生物反应机](nautec:aquatic_biology/bio_reactor.md)中的菌落会稳定产出藻类脂质.

### <Color id="aqua">原油</Color>

在搅拌机中把 1 个藻类脂质与 250 mB 盐水混合, 制成 1,000 mB 原油.

<RecipeFor id="combustion_dynamo"/>
