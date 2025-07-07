# RECIPETYPES

> List of json formats for custom recipes.

## AD ASTRA

### Alloying
```json
{
  "type": "ad_astra:alloying",
  "cookingtime": 100,
  "energy": 20,
  "ingredients": [
    {
      "item": "minecraft:iron_ingot"
    },
    {
      "tag": "minecraft:coals"
    }
  ],
  "result": {
    "count": 1,
    "id": "ad_astra:steel_ingot"
  }
}
```
### Compressing
```json
{
  "type": "ad_astra:compressing",
  "cookingtime": 100,
  "energy": 20,
  "ingredient": {
    "item": "minecraft:iron_ingot"
  },
  "result": {
    "count": 1,
    "id": "ad_astra:iron_plate"
  }
}
```
### Cryo Freezing
```json
{
  "type": "ad_astra:cryo_freezing",
  "cookingtime": 60,
  "energy": 40,
  "ingredient": {
    "item": "ad_astra:ice_shard"
  },
  "result": {
    "fluid": "ad_astra:cryo_fuel",
    "millibuckets": 25
  }
}
```
### NASA Workbench
```json
{
  "type": "ad_astra:nasa_workbench",
  "ingredients": [
    {
      "item": "ad_astra:rocket_nose_cone"
    },
    {
      "tag": "ad_astra:steel_blocks"
    },
    {
      "tag": "ad_astra:steel_blocks"
    },
    {
      "tag": "ad_astra:steel_blocks"
    },
    {
      "tag": "ad_astra:steel_blocks"
    },
    {
      "tag": "ad_astra:steel_blocks"
    },
    {
      "tag": "ad_astra:steel_blocks"
    },
    {
      "item": "ad_astra:rocket_fin"
    },
    {
      "item": "ad_astra:steel_tank"
    },
    {
      "item": "ad_astra:steel_tank"
    },
    {
      "item": "ad_astra:rocket_fin"
    },
    {
      "item": "ad_astra:rocket_fin"
    },
    {
      "item": "ad_astra:steel_engine"
    },
    {
      "item": "ad_astra:rocket_fin"
    }
  ],
  "result": {
    "count": 1,
    "id": "ad_astra:tier_1_rocket"
  }
}
```
### Oxygen Loading
```json
{
  "type": "ad_astra:oxygen_loading",
  "cookingtime": 1,
  "energy": 30,
  "input": {
    "ingredient": {
      "tag": "minecraft:water"
    },
    "millibuckets": 100
  },
  "result": {
    "fluid": "ad_astra:oxygen",
    "millibuckets": 4
  }
}
```
### Refining
```json
{
  "type": "ad_astra:refining",
  "cookingtime": 1,
  "energy": 30,
  "input": {
    "ingredient": {
      "tag": "ad_astra:oil"
    },
    "millibuckets": 5
  },
  "result": {
    "fluid": "ad_astra:fuel",
    "millibuckets": 5
  }
}
```
### Space Station
```json
{
  "type": "ad_astra:space_station_recipe",
  "dimension": "ad_astra:moon_orbit",
  "ingredients": [
    {
      "count": 64,
      "ingredient": {
        "tag": "ad_astra:iron_plates"
      }
    },
    {
      "count": 32,
      "ingredient": {
        "tag": "ad_astra:steel_ingots"
      }
    },
    {
      "count": 32,
      "ingredient": {
        "tag": "ad_astra:desh_ingots"
      }
    },
    {
      "count": 32,
      "ingredient": {
        "tag": "ad_astra:desh_plates"
      }
    }
  ],
  "structure": "ad_astra:space_station"
}
```

## AlcoCraft+

### Brewing
```json
{
  "type": "alcocraftplus:beer_brewing",
  "ingredients": [
    {
      "item": "alcocraftplus:hop"
    },
    {
      "item": "alcocraftplus:dry_seeds"
    },
    {
      "item": "minecraft:snowball"
    },
    {
      "item": "minecraft:packed_ice"
    }
  ],
  "output": {
    "item": "alcocraftplus:ice_beer"
  }
}
```

## Applied Energistics 2
### Charger
```json
{
  "type": "ae2:charger",
  "ingredient": {
    "item": "ae2:certus_quartz_crystal"
  },
  "result": {
    "item": "ae2:charged_certus_quartz_crystal"
  }
}
```
### Entropy
```json
{
  "type": "ae2:entropy",
  "input": {
    "fluid": {
      "id": "minecraft:water"
    }
  },
  "mode": "cool",
  "output": {
    "block": {
      "id": "minecraft:ice"
    }
  }
}
```
### Inscriber
```json
{
  "type": "ae2:inscriber",
  "ingredients": {
    "bottom": {
      "item": "ae2:printed_silicon"
    },
    "middle": {
      "item": "minecraft:redstone"
    },
    "top": {
      "item": "ae2:printed_engineering_processor"
    }
  },
  "mode": "press",
  "result": {
    "item": "ae2:engineering_processor"
  }
}
```
### Matter Cannon
```json
{
  "type": "ae2:matter_cannon",
  "ammo": {
    "item": "ae2:matter_ball"
  },
  "weight": 32.0
}
```
### Transform
```json
{
  "type": "ae2:transform",
  "circumstance": {
    "type": "fluid",
    "tag": "minecraft:water"
  },
  "ingredients": [
    {
      "item": "ae2:charged_certus_quartz_crystal"
    },
    {
      "item": "ae2:certus_quartz_dust"
    }
  ],
  "result": {
    "count": 2,
    "item": "ae2:certus_quartz_crystal"
  }
}
```

## Archon

### Scripting
```json
{
  "type": "archon:scripting",
  "ingredients": [
    {
      "item": "minecraft:iron_pickaxe"
    },
    {
      "tag": "minecraft:coals"
    },
    {
      "item": "minecraft:bone_meal"
    }
  ],
  "result": {
    "item": "archon:crush_tome"
  }
}
```
### Channeling
```json
{
  "type": "archon:channeling",
  "tag": "minecraft:diamond_ores",
  "result": {
    "item": "minecraft:diamond",
    "count": 2
  },
  "manaCost": 50
}
```

## Better End

### Alloying
```json
{
  "type": "bclib:alloying",
  "experience": 3.0,
  "ingredients": [
    {
      "tag": "betterend:alloying_copper"
    },
    {
      "tag": "betterend:alloying_copper"
    }
  ],
  "result": {
    "count": 3,
    "item": "minecraft:copper_ingot"
  },
  "smelttime": 350
}
```
### Smithing
```json
{
  "type": "bclib:smithing",
  "anvilLevel": 5,
  "damage": 6,
  "input": {
    "item": "betterend:aeternium_ingot"
  },
  "result": {
    "item": "betterend:aeternium_axe_head"
  },
  "toolLevel": 5
}
```
### Infusing
```json
{
  "type": "betterend:infusion",
  "catalysts": {
    "east": {
      "item": "minecraft:prismarine_crystals"
    },
    "north": {
      "item": "betterend:enchanted_petal"
    },
    "north_east": {
      "item": "minecraft:lapis_lazuli"
    },
    "north_west": {
      "item": "minecraft:lapis_lazuli"
    },
    "south": {
      "item": "minecraft:prismarine_crystals"
    },
    "south_east": {
      "item": "minecraft:lapis_lazuli"
    },
    "south_west": {
      "item": "minecraft:lapis_lazuli"
    },
    "west": {
      "item": "minecraft:prismarine_crystals"
    }
  },
  "group": "enchantment",
  "input": {
    "item": "minecraft:book"
  },
  "result": {
    "item": "minecraft:enchanted_book",
    "nbt": "{StoredEnchantments:[{id:\"minecraft:aqua_affinity\",lvl:1s}]}"
  },
  "time": 300
}
```

## Create

### Compacting
```json
{
  "type": "create:compacting",
  "ingredients": [
    {
      "item": "minecraft:baked_potato"
    },
    {
      "item": "minecraft:baked_potato"
    },
    {
      "item": "minecraft:baked_potato"
    },
    {
      "item": "minecraft:baked_potato"
    },
    {
      "item": "minecraft:baked_potato"
    },
    {
      "item": "minecraft:baked_potato"
    },
    {
      "item": "minecraft:carrot"
    },
    {
      "item": "minecraft:carrot"
    },
    {
      "item": "minecraft:carrot"
    }
  ],
  "results": [
    {
      "amount": 20250,
      "fluid": "create_bic_bit:stamppot"
    }
  ]
}
```
### Deploying
```json
{
  "type": "create:deploying",
  "ingredients": [
    {
      "item": "create_bic_bit:aged_cheese"
    },
    {
      "item": "minecraft:honeycomb_block"
    }
  ],
  "results": [
    {
      "item": "create_bic_bit:waxed_aged_cheese"
    }
  ],
  "keepHeldItem": true
}
```
### Emptying
```json
{
  "type": "create:emptying",
  "ingredients": [
    {
      "item": "create_bic_bit:ketchup_bottle"
    }
  ],
  "results": [
    {
      "item": "minecraft:glass_bottle"
    },
    {
      "amount": 20250,
      "fluid": "create_bic_bit:ketchup"
    }
  ]
}
```
### Filling
```json
{
  "type": "create:filling",
  "ingredients": [
    {
      "item": "minecraft:glass_bottle"
    },
    {
      "amount": 20250,
      "fluid": "create_bic_bit:mayonnaise"
    }
  ],
  "results": [
    {
      "item": "create_bic_bit:mayonnaise_bottle"
    }
  ]
}
```
### Milling
```json
{
  "type": "create:milling",
  "ingredients": [
    {
      "item": "minecraft:nether_wart"
    }
  ],
  "processingTime": 50,
  "results": [
    {
      "item": "create_bic_bit:crushed_nether_wart",
      "count": 1
    }
  ]
}
```
### Mixing
```json
{
  "type": "create:mixing",
  "heatRequirement": "heated",
  "ingredients": [
    {
      "item": "minecraft:sunflower"
    }
  ],
  "results": [
  	{
    "item": "create_bic_bit:sunflower_seeds",
    "count": 1
  },
   {
      "chance": 0.10,
      "count": 1,
      "item": "create_bic_bit:sunflower_seeds"
    }
  ]
}
```
### Blasting
```json
{
  "type": "minecraft:blasting",
  "category": "misc",
  "cookingtime": 100,
  "experience": 0.1,
  "ingredient": {
    "item": "create:crushed_raw_gold"
  },
  "result": "minecraft:gold_ingot"
}
```
### Pressing
```json
{
  "type": "create:pressing",
  "ingredients": [
    {
      "tag": "c:mithril_ingots"
    }
  ],
  "results": [
    {
      "item": "create_dd:mithril_sheet"
    }
  ]
}
```
### Splashing
```json
{
  "type": "create:splashing",
  "ingredients": [
    {
      "item": "create_bic_bit:dirty_paper"
    }
  ],
  "results": [
    {
      "item": "minecraft:paper"
    }
  ]
}
```
### Mechanical Crafting
```json
{
  "type": "create:mechanical_crafting",
  "pattern": [
    " AAA",
    "BADA",
    " AAA"
  ],
  "key": {
    "A": {
      "tag": "c:brass_ingots"
    },
    "B": {
      "item": "create_dd:integrated_mechanism"
    },
    "D": {
      "tag": "create:casing/steel"
    }
  },
  "result": {
    "item": "create_dd:flywheel",
    "count": 1
  },
  "acceptMirrored": true
}
```
### Item Application
```json
{
  "type": "create:item_application",
  "ingredients": [
    {
      "tag": "create:casing/zinc"
    },
    {
      "tag": "c:industrial_iron_plates"
    }
  ],
  "results": [
    {
      "item": "create_dd:industrial_casing"
    }
  ]
}
```
### Crushing
```json
{
  "type": "create:crushing",
  "ingredients": [
    {
      "item": "create_dd:asurine_cobble"
    }
  ],
  "processingTime": 375,
  "results": [
    {
      "chance": 0.12,
      "item": "create:crushed_raw_zinc"
    },
    {
      "chance": 0.12,
      "item": "create:zinc_nugget"
    }
  ]
}
```
### Haunting
```json
{
  "type": "create:haunting",
  "ingredients": [
    {
      "tag": "minecraft:wooden_doors"
    }
  ],
  "results": [
    {
      "item": "create_dd:spirit_door"
    }
  ]
}
```
### Sandpaper Polishing
```json
{
  "type": "create:sandpaper_polishing",
  "ingredients": [
    {
      "item": "create_dd:spectral_ruby"
    }
  ],
  "results": [
    {
      "item": "create_dd:polished_spectral_ruby"
    }
  ]
}
```
### Sequenced Assembly
```json
{
  "type": "create:sequenced_assembly",
  "ingredient": {
    "tag": "c:lapis_alloy_plates"
  },
  "transitionalItem": {
    "item": "create_dd:incomplete_integrated_circuit"
  },
  "sequence": [
    {
      "type": "create:deploying",
      "ingredients": [
        {
          "item": "create_dd:incomplete_integrated_circuit"
        },
        {
          "item": "minecraft:redstone"
        }
      ],
      "results": [
        {
          "item": "create_dd:incomplete_integrated_circuit"
        }
      ]
    },
    {
      "type": "create:deploying",
      "ingredients": [
        {
          "item": "create_dd:incomplete_integrated_circuit"
        },
        {
          "item": "minecraft:quartz"
        }
      ],
      "results": [
        {
          "item": "create_dd:incomplete_integrated_circuit"
        }
      ]
    },
    {
      "type": "create:deploying",
      "ingredients": [
        {
          "item": "create_dd:incomplete_integrated_circuit"
        },
        {
          "tag": "c:brass_nuggets"
        }
      ],
      "results": [
        {
          "item": "create_dd:incomplete_integrated_circuit"
        }
      ]
    }
  ],
  "results": [
    {
      "item": "create_dd:integrated_circuit",
      "chance": 160.0
    },
    {
      "item": "create_dd:lapis_sheet",
      "chance": 5.0
    },
    {
      "item": "minecraft:redstone",
      "chance": 2.5
    },
    {
        "item": "minecraft:quartz",
      "chance": 2.5
    },
    {
      "item": "create:brass_nugget",
      "chance": 2.5
    }
  ],
  "loops": 4
}
```
### Cutting
```json
{
  "type": "create:cutting",
  "ingredients": [
    {
      "item": "create:copper_sheet"
    }
  ],
  "results": [
    {
      "item": "create_new_age:copper_wire",
      "count": 4
    }
  ],
  "processingTime": 100
}
```


## Create Bitterballen

### Deep Frying
```json
{
  "type": "create_bic_bit:deep_frying",
  "heatRequirement": "heated",
  "ingredients": [
    {
      "item": "create_bic_bit:raw_eggball"
    },
    {
      "amount": 10125,
      "fluid": "create_bic_bit:frying_oil"
    }
  ],
  "processingTime": 100,
  "results": [
    {
      "item": "create_bic_bit:eggball"
    }
  ]
}
```

## Create Dreams & Desires

### Freezing
```json
{
  "type": "create_dd:freezing",
  "ingredients": [
    {
      "item": "minecraft:water_bucket"
    }
  ],
  "results": [
    {
      "item": "minecraft:powder_snow_bucket",
      "count": 1
    }
  ]
}
```
### Superheating
```json
{
  "type": "create_dd:superheating",
  "ingredients": [
    {
      "item": "create:crushed_raw_gold"
    }
  ],
  "results": [
    {
      "item": "minecraft:gold_ingot"
    },
    {
      "chance": 0.5,
      "item": "minecraft:gold_ingot"
    }
  ]
}
```

## Create Enchantment Industry

### Disenchanting
```json
{
  "type": "create_enchantment_industry:disenchanting",
  "ingredients": [
    {
      "item": "create:experience_nugget"
    }
  ],
  "results": [
    {
      "fluid": "create_enchantment_industry:experience",
      "amount": 243
    }
  ]
}
```

## Create New Age

### Energizing
```json
{
  "type": "create_new_age:energising",
  "energy_needed": 2000,
  "ingredients": [
    {
      "item": "minecraft:gold_ingot"
    }
  ],
  "results": [
    {
      "item": "create_new_age:overcharged_gold"
    }
  ]
}
```

## Create Additions

### Charging
```json
{
	"type":"createaddition:charging",
	"input": {
      	"item": "create:exposed_copper_shingles",
		"count": 1
	},
	"result": {
		"item": "create:copper_shingles",
		"count": 1
	},
	"energy": 4000,
	"maxChargeRate": 200
}
```
### Liquid Burning
```json
{
	"type":"createaddition:liquid_burning",
	"input": {
      	"fluidTag": "c:diesel",
      	"amount": 81000
	},
	"burnTime": 48000,
	"superheated": true,
	"fabric:load_conditions": [
		{
			"condition": "fabric:fluid_tags_populated",
			"values": [
				"c:diesel"
			]
		}
	]
}
```
### Rolling
```json
{
	"type":"createaddition:rolling",
	"input": {
      	"tag": "c:iron_plates"
	},
	"result": {
		"item": "createaddition:iron_wire",
		"count": 2
	}
}
```

## Create Big Cannons

### Melting
```json
{
  "fabric:load_conditions": [
    {
      "condition": "fabric:item_tags_populated",
      "values": [
        "createbigcannons:block_bronze"
      ]
    }
  ],
  "type": "createbigcannons:melting",
  "heatRequirement": "heated",
  "ingredients": [
    {
      "tag": "createbigcannons:block_bronze"
    }
  ],
  "processingTime": 1620,
  "results": [
    {
      "amount": 65610,
      "fluid": "createbigcannons:molten_bronze"
    }
  ]
}
```

## Create Diesel Generators

### Basin Fermenting
```json
{
  "type": "createdieselgenerators:basin_fermenting",
  "ingredients": [
    {
      "item": "create:wheat_flour"
    },
    {
      "fluid": "minecraft:water",
      "amount": 8100
    }
  ],
  "processingTime": 200,
  "results": [
    {
      "item": "create:dough"
    },
    {
      "item": "create:wheat_flour",
      "chance": 0.1
    }
  ]
}
```
### Distillation
```json
{
  "type": "createdieselgenerators:distillation",
  "ingredients": [
    {
      "fluidTag": "c:crude_oil",
      "amount": 8100
    }
  ],
  "heatRequirement": "heated",
  "processingTime": 100,
  "results": [
    {
      "fluid": "createdieselgenerators:diesel",
      "amount": 4050
    },
    {
      "fluid": "createdieselgenerators:gasoline",
      "amount": 4050
    }
  ]
}
```

## Create Estrogen

### Centrifuging
```json
{
  "type": "estrogen:centrifuging",
  "ingredients": [
    {
      "amount": 81,
      "fluid": "estrogen:filtrated_horse_urine",
      "nbt": {}
    }
  ],
  "results": [
    {
      "amount": 81,
      "fluid": "estrogen:liquid_estrogen"
    }
  ]
}
```

## Farmers Delight

> todo ...

###
```json
```
###
```json
```

## Tech Reborn

### Alloy Smelter
```json
{
  "type": "techreborn:alloy_smelter",
  "ingredients": [
    {
      "count": 3,
      "item": "minecraft:copper_ingot"
    },
    {
      "tag": "c:zinc_ingots"
    }
  ],
  "power": 6,
  "results": [
    {
      "count": 4,
      "item": "techreborn:brass_ingot"
    }
  ],
  "time": 200
}
```
### Assembling Machine
```json
{
  "type": "techreborn:assembling_machine",
  "power": 20,
  "time": 200,
  "ingredients": [
    {
      "tag": "c:silicon_plates"
    },
    {
      "tag": "c:electrum_plates",
      "count": 2
    }
  ],
  "results": [
    {
      "item": "techreborn:advanced_circuit"
    }
  ]
}
```
### Blast Furnace
```json
{
  "type": "techreborn:blast_furnace",
  "power": 128,
  "time": 1000,
  "heat": 1500,
  "ingredients": [
	{
	  "item": "techreborn:quartz_dust",
	  "count": 2
	},
	{
	  "fluid": "techreborn:carbon",
	  "holder": "techreborn:cell",
	  "count": 4
	}
  ],
  "results": [
	{
	  "item": "techreborn:cell",
	  "count": 2,
	  "nbt": {
		"fluid": "techreborn:silicon"
	  }
	},
	{
	  "item": "techreborn:cell",
	  "count": 2,
	  "nbt": {
		"fluid": "techreborn:compressed_air"
	  }
	}
  ]
}
```
### Centrifuge
```json
{
  "type": "techreborn:centrifuge",
  "power": 5,
  "time": 2500,
  "ingredients": [
    {
      "item": "minecraft:soul_sand",
      "count": 16
    },
    {
      "item": "techreborn:cell",
      "nbt": "null"
    }
  ],
  "results": [
    {
      "item": "minecraft:sand",
      "count": 10
    },
    {
      "item": "techreborn:saltpeter_dust",
      "count": 4
    },
    {
      "item": "techreborn:coal_dust"
    },
    {
      "item": "techreborn:cell",
      "nbt": {
        "fluid": "techreborn:oil"
      }
    }
  ]
}
```
### Chemical Reactor
```json
{
  "type": "techreborn:chemical_reactor",
  "power": 30,
  "time": 800,
  "ingredients": [
    {
      "fluid": "techreborn:carbon",
      "holder": "techreborn:cell"
    },
    {
      "fluid": "techreborn:calcium",
      "holder": "techreborn:cell"
    }
  ],
  "results": [
    {
      "item": "techreborn:cell",
      "count": 2,
      "nbt": {
        "fluid": "techreborn:calcium_carbonate"
      }
    }
  ]
}
```
### Compressor
```json
{
  "type": "techreborn:compressor",
  "power": 10,
  "time": 300,
  "ingredients": [
    {
      "tag": "c:calcite_small_dusts",
      "count": 5
    }
  ],
  "results": [
    {
      "item": "minecraft:calcite"
    }
  ]
}
```
### Distillation Tower
```json
{
  "type": "techreborn:distillation_tower",
  "power": 20,
  "time": 400,
  "ingredients": [
    {
      "item": "techreborn:cell",
      "count": 16,
      "nbt": "empty"
    },
    {
      "fluid": "techreborn:oil",
      "holder": "techreborn:cell",
      "count": 16
    }
  ],
  "results": [
    {
      "item": "techreborn:cell",
      "count": 16,
      "nbt": {
        "fluid": "techreborn:diesel"
      }
    },
    {
      "item": "techreborn:cell",
      "count": 15,
      "nbt": {
        "fluid": "techreborn:sulfuric_acid"
      }
    },
    {
      "item": "techreborn:cell",
      "nbt": {
        "fluid": "techreborn:glyceryl"
      }
    }
  ]
}
```
### Extractor
```json
{
  "type": "techreborn:extractor",
  "ingredients": [
    {
      "item": "minecraft:gravel"
    }
  ],
  "power": 2,
  "results": [
    {
      "item": "minecraft:flint"
    }
  ],
  "time": 200
}
```
### Fluid Replicator
```json
{
  "type": "techreborn:fluid_replicator",
  "power": 40,
  "time": 200,
  "tank": {
    "fluid": "techreborn:glyceryl",
    "amount": 1000
  },
  "ingredients": [
    {
      "item": "techreborn:uu_matter",
      "count": 8
    }
  ],
  "results": []
}
```
### Fusion Reactor
```json
{
	"type": "techreborn:fusion_reactor",
	"power": 16384,
	"time": 2048,
	"start-power": 40000000,
	"min-size": 1,
	"ingredients": [
		{
			"fluid": "techreborn:helium3",
			"holder": "techreborn:cell"
		},
		{
			"fluid": "techreborn:deuterium",
			"holder": "techreborn:cell"
		}
	],
	"results": [
		{
			"item": "techreborn:cell",
			"nbt":{
				"fluid": "techreborn:heliumplasma"
			}
		}
	]
}
```
### Grinder
```json
{
  "type": "techreborn:grinder",
  "ingredients": [
    {
      "tag": "c:coal_ores"
    }
  ],
  "power": 2,
  "results": [
    {
      "count": 2,
      "item": "minecraft:coal"
    }
  ],
  "time": 200
}
```
### Implosion Compressor
```json
{
  "type": "techreborn:implosion_compressor",
  "power": 30,
  "time": 2000,
  "ingredients" : [
	{
	  "item": "techreborn:iridium_alloy_ingot"
	},
    {
      "item": "minecraft:tnt",
      "count": 8
    }
  ],
  "results" : [
    {
      "item": "techreborn:iridium_alloy_plate"
    },
    {
      "item": "techreborn:dark_ashes_dust",
      "count": 4
    }
  ]
}
```
### Industrial Electrolyzer
```json
{
  "type": "techreborn:industrial_electrolyzer",
  "power": 50,
  "time": 2200,
  "ingredients": [
    {
      "item": "techreborn:uvarovite_dust",
      "count": 20
    },
    {
      "item": "techreborn:cell",
      "count": 12,
      "nbt": "empty"
    }
  ],
  "results": [
    {
      "item": "techreborn:cell",
      "count": 3,
      "nbt": {
        "fluid": "techreborn:calcium"
      }
    },
    {
      "item": "techreborn:chrome_dust",
      "count": 2
    },
    {
      "item": "techreborn:cell",
      "count": 3,
      "nbt": {
        "fluid": "techreborn:silicon"
      }
    },
    {
      "item": "techreborn:cell",
      "count": 6,
      "nbt": {
        "fluid": "techreborn:compressed_air"
      }
    }
  ]
}
```
### Industrial Grinder
```json
{
  "type": "techreborn:industrial_grinder",
  "power": 64,
  "time": 100,
  "tank": {
    "fluid": "techreborn:sodium_persulfate",
    "amount": 1000
  },
  "ingredients": [
    {
      "tag": "c:tin_ores"
    }
  ],
  "results": [
    {
      "item": "techreborn:raw_tin",
      "count": 2
    },
    {
      "item": "minecraft:raw_iron"
    },
    {
      "item": "techreborn:zinc_dust"
    }
  ]
}
```
### Industrial Sawmill
```json
{
  "type": "techreborn:industrial_sawmill",
  "ingredients": [
    {
      "tag": "minecraft:oak_logs"
    }
  ],
  "power": 40,
  "results": [
    {
      "count": 4,
      "item": "minecraft:oak_planks"
    },
    {
      "count": 3,
      "item": "techreborn:saw_dust"
    }
  ],
  "tank": {
    "amount": {
      "droplets": 81000
    },
    "fluid": "minecraft:water"
  },
  "time": 200
}
```
### Rolling Machine
```json
{
  "type": "techreborn:rolling_machine",
  "shaped": {
    "pattern": [
      " N ",
      "NCN",
      " N "
    ],
    "key": {
      "N": {
        "tag": "c:nickel_ingots"
      },
      "C": {
        "tag": "c:chromium_ingots"
      }
    },
    "result": {
      "item": "techreborn:nichrome_heating_coil",
      "count": 2
    }
  },
  "power": 5,
  "time": 250
}
```
### Scrap Box
```json
{
  "power": 10,
  "time": 20,
  "ingredients": [
    {
      "item": "techreborn:scrap_box"
    }
  ],
  "results": [
    {
      "item": "minecraft:redstone"
    }
  ],
  "type": "techreborn:scrapbox"
}
```
### Solid Canning Machine
```json
{
	"type": "techreborn:solid_canning_machine",
	"power": 1,
	"time": 60,
	"ingredients": [
		{
			"fluid": "techreborn:helium",
			"holder": "techreborn:cell"
		},
		{
			"tag": "c:tin_ingots",
			"count": 2
		}
	],
	"results": [
		{
			"item": "techreborn:helium_coolant_cell_60k"
		}
	]
}
```
### Vacuum Freezer
```json
{
  "type": "techreborn:vacuum_freezer",
  "power": 60,
  "time": 440,
  "ingredients": [
    {
      "fluid": "techreborn:heliumplasma",
      "holder": "techreborn:cell"
    }
  ],
  "results": [
    {
      "item": "techreborn:cell",
      "nbt": {
        "fluid": "techreborn:helium"
      }
    }
  ]
}
```
### Wiremill
```json
{
  "type": "techreborn:wire_mill",
  "power": 2,
  "time": 200,
  "ingredients": [
    {
      "item": "minecraft:copper_ingot"
    }
  ],
  "results": [
    {
      "item": "techreborn:copper_cable",
      "count": 6
    }
  ]
}
```
### Recycler
```json
{
  "type": "techreborn:recycler",
  "power": 2,
  "time": 25,
  "ingredients": [
  ],
  "results": [
	{
	  "item": "techreborn:scrap"
	}
  ]
}


```
###
```json
```
###
```json
```
###
```json
```


## Minecraft

### Smithing Transform
```json
{
  "type": "minecraft:smithing_transform",
  "addition": {
    "item": "betterend:aeternium_ingot"
  },
  "base": {
    "item": "minecraft:elytra"
  },
  "result": {
    "item": "betterend:elytra_armored"
  },
  "template": {
    "item": "betterend:aeternium_upgrade_smithing_template"
  }
}
```
### Stonecutting
```json
{
  "type": "minecraft:stonecutting",
  "count": 1,
  "group": "azure_jadestone_stonecutting",
  "ingredient": {
    "item": "betterend:azure_jadestone"
  },
  "result": "betterend:azure_jadestone_bricks_stairs"
}
```
### Crafting Shaped
```json
{
  "type": "minecraft:crafting_shaped",
  "category": "misc",
  "group": "end_bricks",
  "key": {
    "#": {
      "item": "betterend:azure_jadestone"
    }
  },
  "pattern": [
    "##",
    "##"
  ],
  "result": {
    "count": 4,
    "item": "betterend:azure_jadestone_bricks"
  },
  "show_notification": true
}
```
### Crafting Shapeless
```json
{
  "type": "minecraft:crafting_shapeless",
  "category": "misc",
  "ingredients": [
    {
      "item": "betterend:blue_vine_seed"
    }
  ],
  "result": {
    "item": "minecraft:blue_dye"
  }
}
```
### Smelting
```json
{
  "type": "minecraft:smelting",
  "category": "food",
  "cookingtime": 200,
  "experience": 0.0,
  "ingredient": {
    "item": "betterend:chorus_mushroom_raw"
  },
  "result": "betterend:chorus_mushroom_cooked"
}
```
### Campfire Cooking
```json
{
  "type": "minecraft:campfire_cooking",
  "group": "food",
  "category": "food",
  "experience": 0,
  "cookingtime": 600,
  "ingredient": {
    "item": "create_bic_bit:sunflower_seeds"
  },
  "result": "create_bic_bit:roasted_sunflower_seeds"
}
```
### Smoking
```json
{
  "type": "minecraft:smoking",
  "cookingtime": 50,
  "experience": 0.0,
  "ingredient": {
    "item": "create_dd:frozen_nugget"
  },
  "result": "create:experience_nugget"
}
```
