---
navigation:
  title: 生态缸
  icon: nautec:biome_tank
  position: 20
  parent: getting_started/getting_started-index.md
item_ids:
  - nautec:biome_tank
---

# <Color id="light_purple">生态缸</Color>

<Column alignItems="center" fullWidth={true}>
  <ItemImage id="biome_tank" scale="2"/>
  一个密封的玻璃缸, 里面装着一个小型生物群系的片段.
</Column>

生态缸可以自行种植一种植物, 无需能量, 水或光照, 因此你可以种植自己并不身处其中的生物群系里的植物.

***

## <Color id="gold">为生态缸接种</Color>

手持植物右键点击生态缸即可接种. 这会消耗一个该植物, 此后生态缸会种植该植物. 手持另一种植物右键点击可切换: 它已经种出的东西会先返还给你.

破坏生态缸后它会保留其中的植物, 因此你可以把它捡起搬走, 无需再次接种.

<RecipeFor id="biome_tank"/>

***

## <Color id="gold">生长</Color>

已接种的生态缸每 30 秒生长一个该植物(`config/nautec-common.toml` 中的 `biomeTankTicks`), 最多可存放一组. 空手右键点击可取走它已种出的东西, 也可以用漏斗或管道从任意一面抽出. 无法向其中放入任何物品. 存满一组后生态缸会停止, 直到你清空它.

***

## <Color id="gold">植物</Color>

| 植物 | 生成于 |
|---|---|
| <ItemImage id="nautec:glow_polyp" scale="0.5"/> 荧光珊瑚虫 | 荧光海林 |
| <ItemImage id="nautec:luminescent_algae" scale="0.5"/> 荧光藻 | 荧光海林 |
| <ItemImage id="nautec:deep_kelp" scale="0.5"/> 深海海带 | 荧光海林 |
| <ItemImage id="nautec:prismarine_frond" scale="0.5"/> 海晶叶丛 | 海晶礁 |
| <ItemImage id="nautec:abyssal_coral" scale="0.5"/> 深渊珊瑚 | 深渊海沟 |
| <ItemImage id="nautec:vent_tubeworm" scale="0.5"/> 热泉管虫 | 海底热泉 |
| <ItemImage id="minecraft:kelp" scale="0.5"/> 海带 | 海洋 |
| <ItemImage id="minecraft:seagrass" scale="0.5"/> 海草 | 海洋 |
| <ItemImage id="minecraft:sea_pickle" scale="0.5"/> 海泡菜 | 暖水海洋 |
| <ItemImage id="minecraft:tube_coral" scale="0.5"/> 管珊瑚 | 暖水海洋 |
| <ItemImage id="minecraft:brain_coral" scale="0.5"/> 脑纹珊瑚 | 暖水海洋 |
| <ItemImage id="minecraft:bubble_coral" scale="0.5"/> 气泡珊瑚 | 暖水海洋 |
| <ItemImage id="minecraft:fire_coral" scale="0.5"/> 火珊瑚 | 暖水海洋 |
| <ItemImage id="minecraft:horn_coral" scale="0.5"/> 角珊瑚 | 暖水海洋 |
| <ItemImage id="minecraft:cactus" scale="0.5"/> 仙人掌 | 沙漠 |
| <ItemImage id="minecraft:sugar_cane" scale="0.5"/> 甘蔗 | 河岸 |
| <ItemImage id="minecraft:bamboo" scale="0.5"/> 竹子 | 丛林 |
| <ItemImage id="minecraft:sweet_berries" scale="0.5"/> 甜浆果 | 针叶林 |
| <ItemImage id="minecraft:glow_berries" scale="0.5"/> 发光浆果 | 繁茂洞穴 |
| <ItemImage id="minecraft:red_mushroom" scale="0.5"/> 红色蘑菇 | 蘑菇岛 |
| <ItemImage id="minecraft:brown_mushroom" scale="0.5"/> 棕色蘑菇 | 蘑菇岛 |
| <ItemImage id="minecraft:crimson_fungus" scale="0.5"/> 绯红菌 | 绯红森林 |
| <ItemImage id="minecraft:warped_fungus" scale="0.5"/> 诡异菌 | 诡异森林 |
| <ItemImage id="minecraft:chorus_fruit" scale="0.5"/> 紫颂果 | 末地 |
| <ItemImage id="minecraft:cocoa_beans" scale="0.5"/> 可可豆 | 丛林 |

***

## <Color id="gold">供整合包作者参考</Color>

生态缸接受的植物由物品标签 `nautec:biome_tank_plants` 决定. 通过数据包或 KubeJS 可以把任何模组的任何物品加入该标签, 生态缸就会种植它. 生态缸在玻璃内使用植物自身的物品模型来显示植物, 因此模组植物无需额外纹理. 把某种植物从标签中移除后, 已经在种植它的生态缸会停止.
