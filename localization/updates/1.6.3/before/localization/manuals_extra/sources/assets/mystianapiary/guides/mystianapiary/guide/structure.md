---
navigation:
  title: Apiary Structure
  parent: index.md
  icon: minecraft:honeycomb_block
  position: 1
---

# Apiary Structure

The Mystian Apiary is a **3x3x3 multiblock** that runs your Productive Bees in place, so no bees ever leave it.

At its heart is a **Honeycomb Block**, wrapped in a cube of **logs**, with the four boxes set into its sides.

## The Build

Working out from the middle:

- **Center**: a Honeycomb Block
- **North, south, east, west** of it: one each of the [Bee Box](modules.md#bee-box), [Flower Box](modules.md#flower-box), [Storage](modules.md#storage), and [Controller](modules.md#controller), in any arrangement
- **Every other spot** in the cube: any logs, normal or stripped

<GameScene zoom="6">
  <Block x="0" y="0" z="0" id="minecraft:oak_log" />
  <Block x="1" y="0" z="0" id="minecraft:oak_log" />
  <Block x="2" y="0" z="0" id="minecraft:oak_log" />
  <Block x="0" y="0" z="1" id="minecraft:oak_log" />
  <Block x="1" y="0" z="1" id="minecraft:oak_log" />
  <Block x="2" y="0" z="1" id="minecraft:oak_log" />
  <Block x="0" y="0" z="2" id="minecraft:oak_log" />
  <Block x="1" y="0" z="2" id="minecraft:oak_log" />
  <Block x="2" y="0" z="2" id="minecraft:oak_log" />
  <Block x="0" y="1" z="0" id="minecraft:oak_log" />
  <Block x="1" y="1" z="0" id="mystianapiary:input_block" p:facing="west" />
  <Block x="2" y="1" z="0" id="minecraft:oak_log" />
  <Block x="0" y="1" z="1" id="mystianapiary:flower_block" p:facing="south" />
  <Block x="1" y="1" z="1" id="minecraft:honeycomb_block" />
  <Block x="2" y="1" z="1" id="mystianapiary:upgrade_block" />
  <Block x="0" y="1" z="2" id="minecraft:oak_log" />
  <Block x="1" y="1" z="2" id="mystianapiary:output_block" p:facing="east" />
  <Block x="2" y="1" z="2" id="minecraft:oak_log" />
  <Block x="0" y="2" z="0" id="minecraft:oak_log" />
  <Block x="1" y="2" z="0" id="minecraft:oak_log" />
  <Block x="2" y="2" z="0" id="minecraft:oak_log" />
  <Block x="0" y="2" z="1" id="minecraft:oak_log" />
  <Block x="1" y="2" z="1" id="minecraft:oak_log" />
  <Block x="2" y="2" z="1" id="minecraft:oak_log" />
  <Block x="0" y="2" z="2" id="minecraft:oak_log" />
  <Block x="1" y="2" z="2" id="minecraft:oak_log" />
  <Block x="2" y="2" z="2" id="minecraft:oak_log" />
</GameScene>

## Optional: A Second Storage Box

Need more room? The log **directly above the Honeycomb Block** (top-center) may be replaced with a **second Storage box** of any tier. Produce fills the main side box first and only spills into the second once that box is full, though a partly filled stack in the second box is always topped up first. Fluids overflow the same way.

A log there is still perfectly fine, the second box is entirely optional (server owners can disable it with the `allowSecondOutput` config).

<GameScene zoom="6">
  <Block x="0" y="0" z="0" id="minecraft:oak_log" />
  <Block x="1" y="0" z="0" id="minecraft:oak_log" />
  <Block x="2" y="0" z="0" id="minecraft:oak_log" />
  <Block x="0" y="0" z="1" id="minecraft:oak_log" />
  <Block x="1" y="0" z="1" id="minecraft:oak_log" />
  <Block x="2" y="0" z="1" id="minecraft:oak_log" />
  <Block x="0" y="0" z="2" id="minecraft:oak_log" />
  <Block x="1" y="0" z="2" id="minecraft:oak_log" />
  <Block x="2" y="0" z="2" id="minecraft:oak_log" />
  <Block x="0" y="1" z="0" id="minecraft:oak_log" />
  <Block x="1" y="1" z="0" id="mystianapiary:input_block" p:facing="west" />
  <Block x="2" y="1" z="0" id="minecraft:oak_log" />
  <Block x="0" y="1" z="1" id="mystianapiary:flower_block" p:facing="south" />
  <Block x="1" y="1" z="1" id="minecraft:honeycomb_block" />
  <Block x="2" y="1" z="1" id="mystianapiary:upgrade_block" />
  <Block x="0" y="1" z="2" id="minecraft:oak_log" />
  <Block x="1" y="1" z="2" id="mystianapiary:output_block" p:facing="east" />
  <Block x="2" y="1" z="2" id="minecraft:oak_log" />
  <Block x="0" y="2" z="0" id="minecraft:oak_log" />
  <Block x="1" y="2" z="0" id="minecraft:oak_log" />
  <Block x="2" y="2" z="0" id="minecraft:oak_log" />
  <Block x="0" y="2" z="1" id="minecraft:oak_log" />
  <Block x="1" y="2" z="1" id="mystianapiary:output_block" p:facing="north" />
  <Block x="2" y="2" z="1" id="minecraft:oak_log" />
  <Block x="0" y="2" z="2" id="minecraft:oak_log" />
  <Block x="1" y="2" z="2" id="minecraft:oak_log" />
  <Block x="2" y="2" z="2" id="minecraft:oak_log" />
</GameScene>
