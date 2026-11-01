---
navigation:
  title: 渗透过滤器
  icon: nautec:osmosis_filter
  position: 5
  parent: laser_chemistry/laser_chemistry-index.md
item_ids:
  - nautec:osmosis_filter
---

# <Color id="light_purple">渗透过滤器</Color>

<Column alignItems="center" fullWidth={true}>
  <ItemImage id="osmosis_filter" scale="2"/>
  无需燃料, 原料或光束, 即可自行产水.
</Column>

## <Color id="gold">使用</Color>

放在任意位置后, 就会以每秒 1,000 mB(1 桶)的速度向储罐产水. 储罐达到 16,000 mB(16 桶, 可配置)时停止. 过滤时正面的面板会亮起.

* 手持空桶右击可取出 1,000 mB 水. 其他流体容器也可使用.
* 管道可从任意一面抽水, 无法向内输入任何东西.
* 默认每面都会输出水. [侧面配置](nautec:getting_started/utilities.md)可分别开关各面.

空手右击可查看储罐, 每秒产水量及输入 AP. Jade 也会显示储罐和产水速度.

将水与盐送入[搅拌机](mixer.md)可制作盐水, 也可以送入[内燃发电机](nautec:getting_started/combustion_dynamo.md).

***

## <Color id="gold">更强的光束</Color>

渗透过滤器不需要光束, 但从任意面输入激光束可以加速: 每 40 AP 使产水量翻倍, 最高每秒 1,024,000 mB(两者均可配置).

| 光束 | 每秒产水量 |
|---|---|
| 无 | 1,000 mB |
| 40 AP | 2,000 mB |
| 80 AP | 4,000 mB |
| 160 AP | 16,000 mB |
| 320 AP | 256,000 mB |
| 400 AP | 1,024,000 mB |

当光束使每秒产量超过 16,000 mB 时, 储罐容量会改为一秒的产量, 防止两次抽取之间因装满而停工. 光束减弱时, 储罐内已有的水会保留; 只是停止继续产水, 直到你取出一部分.

更强光束可加速的所有机器见[更强的光束](nautec:getting_started/stronger_beams.md).

<RecipeFor id="osmosis_filter"/>
