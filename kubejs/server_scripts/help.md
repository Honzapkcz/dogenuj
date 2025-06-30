```js
event.shaped(
  Item.of('minecraft:stone', 3), // arg 1: output
  [
    'A B',
    ' C ', // arg 2: the shape (array of strings)
    'B A'
  ],
  {
    A: 'minecraft:andesite',
    B: 'minecraft:diorite',  //arg 3: the mapping object
    C: 'minecraft:granite'
  }
)

event.shapeless(
  Item.of('minecraft:dandelion', 3), // arg 1: output
  [
    'minecraft:bone_meal',
    'minecraft:yellow_dye', 	       // arg 2: the array of inputs
    '3x minecraft:ender_pearl'
  ]
)

event.smithing(
  'minecraft:netherite_ingot',                     // arg 1: output
  'minecraft:netherite_upgrade_smithing_template', // arg 2: the smithing template
  'minecraft:iron_ingot',                          // arg 3: the item to be upgraded
  'minecraft:black_dye'                            // arg 4: the upgrade item
)

// Cook 1 stone into 3 gravel in a Furnace:
event.smelting('3x minecraft:gravel', 'minecraft:stone')

// Blast 1 iron ingot into 10 nuggets in a Blast Furnace: 
event.blasting('10x minecraft:iron_nugget', 'minecraft:iron_ingot')

// Smoke glass into tinted glass in the Smoker and give 0.35XP:
event.smoking('minecraft:tinted_glass', 'minecraft:glass').xp(0.35)

// Burn sticks into torches on the Campfire, give 0.35XP and take 30 seconds:
event.campfireCooking('minecraft:torch', 'minecraft:stick', 0.35, 600)

//allow cutting 3 sticks from any plank on the stonecutter
event.stonecutting('3x minecraft:stick', '#minecraft:planks')

// Slice cake on a cutting board!
event.custom({
  type: 'farmersdelight:cutting',
  ingredients: [
    { item: 'minecraft:cake' }
  ],
  tool: { tag: 'forge:tools/knives' },
  result: [
    { item: 'farmersdelight:cake_slice', count: 7 }
  ]
})

// Adding the Molten Electrum alloying recipe from Tinkers' Construct
event.custom({
  type: 'tconstruct:alloy',
  inputs: [
    { tag: 'forge:molten_gold', amount: 90 },
    { tag: 'forge:molten_silver', amount: 90 }
  ],
  result: { fluid: 'tconstruct:molten_electrum', amount: 180 },
  temperature: 760
})
```

```js
// A blank condition removes all recipes (obviously not recommended):
event.remove({})

// Remove all recipes where output is stone pickaxe:
event.remove({ output: 'minecraft:stone_pickaxe' })

// Remove all recipes where output has the Wool tag:
event.remove({ output: '#minecraft:wool' })

// Remove all recipes where any input has the Redstone Dust tag:
event.remove({ input: '#forge:dusts/redstone' })

// Remove all recipes from Farmer's Delight:
event.remove({ mod: 'farmersdelight' })

// Remove all campfire cooking recipes:
event.remove({ type: 'minecraft:campfire_cooking' })

// Remove all recipes that grant stone EXCEPT smelting recipes:
event.remove({ not: { type: 'minecraft:smelting' }, output: 'stone' })

// Remove recipes that output cooked chicken AND are cooked on a campfire:
event.remove({ output: 'minecraft:cooked_chicken', type: 'minecraft:campfire_cooking' })

// Remove any blasting OR smelting recipes that output minecraft:iron_ingot:
event.remove([{ type: 'minecraft:smelting', output: 'minecraft:iron_ingot' }, { type: 'minecraft:blasting', output: 'minecraft:iron_ingot' }])

// Remove a recipe by ID. in this case, data/minecraft/recipes/glowstone.json:
// Note: Recipe ID and output are usually different!
event.remove({ id: 'minecraft:glowstone' })
```

```js
event.replaceInput(
  { input: 'minecraft:stick' }, // Arg 1: the filter
  'minecraft:stick',            // Arg 2: the item to replace
  '#minecraft:saplings'         // Arg 3: the item to replace it with
  // Note: tagged fluid ingredients do not work on Fabric, but tagged items do.
)
```