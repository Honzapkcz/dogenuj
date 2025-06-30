// priority: 0

console.info('Hello, early_game!')

ServerEvents.recipes(e => {
    /* SMELTING RAW IRON/TIN */
    e.shapeless(
        Item.of("kubejs:dirty_crushed_iron"),
        [
            "minecraft:raw_iron",
            "#create:pickaxes"
        ]
    )
    e.shapeless(
        Item.of("kubejs:dirty_crushed_iron"),
        [
            "#c:raw_tin_ores",
            "#create:pickaxes"
        ]
    )
    e.custom({
        type: "ae2:transform",
        circumstance: {
            type: "fluid",
            tag: "minecraft:water"
        },
        ingredients: [
            {
                item: "kubejs:dirty_crushed_iron"
            },
        ],
        result: {
            item: "create:crushed_raw_iron"
        }
    })
    e.custom({
        type: "ae2:transform",
        circumstance: {
            type: "fluid",
            tag: "minecraft:water"
        },
        ingredients: [
            {
                item: "kubejs:dirty_crushed_tin"
            },
        ],
        result: {
            item: "create_ironworks:crushed_raw_tin"
        }
    })

    /* CRAFTING TABLE */
    e.remove({id: "minecraft:crafting_table"})
    e.shaped(
        Item.of("minecraft:crafting_table"),
        [
            "SS",
            "AK"
        ],
        {
            S: "#minecraft:logs",
            A: "minecraft:wooden_axe",
            K: "farmersdelight:flint_knife"
        }
    )

    /* PADDING AND BED */
    e.remove({output: "#travelersbackpack:sleeping_bags", input: "#minecraft:wool"})
    e.remove({output: "#minecraft:beds", type: "minecraft:crafting", input: "#minecraft:wool"})
    e.shaped(
        Item.of("kubejs:padding"),
        [
            " C ",
            "SWS",
            " C ",
        ],
        {
            C: "farmersdelight:canvas",
            S: "minecraft:stick",
            W: "#minecraft:wool"
        }
    )
    e.shaped(
        Item.of("minecraft:white_bed"),
        [
            "PPP",
            "WWW"
        ],
        {
            P: "kubejs:padding",
            W: "#minecraft:planks"
        }
    )
    e.shaped(
        Item.of("travelersbackpack:white_sleeping_bag"),
        [
            "PPP"
        ],
        {
            P: "kubejs:padding"
        }
    )
    /* FLINT/IRON TOOLS */

    // TODO: hammer and paxel
    for (mat in ["wooden", "stone"]) {
        e.remove({id: "minecraft:"+mat+"_shovel"})
        e.remove({id: "minecraft:"+mat+"_pickaxe"})
        e.remove({id: "minecraft:"+mat+"_axe"})
        e.remove({id: "minecraft:"+mat+"_hoe"})
        e.remove({id: "minecraft:"+mat+"_sword"})
    }
    for (mat in ["iron", "copper", "bronze", "brass", "steel"]) {
        e.remove({id: "minecraft:"+mat+"_shovel"})
        e.remove({id: "minecraft:"+mat+"_pickaxe"})
        e.remove({id: "minecraft:"+mat+"_axe"})
        e.remove({id: "minecraft:"+mat+"_hoe"})
        e.remove({id: "minecraft:"+mat+"_sword"})
        e.remove({id: "create_ironworks:"+mat+"_paxel"})
        e.remove({id: "create_ironworks:"+mat+"_hammer"})
    }
    e.remove({id: "farmersdelight:flint_knife"})
    e.remove({id: "farmersdelight:iron_knife"})

    e.shaped(Item.of("minecraft:wooden_shovel"),
        [" F", "ST"],
        {F: "minecraft:flint", S: "minecraft:string", T: "minecraft:stick"}
    )
    e.shaped(Item.of("minecraft:wooden_pickaxe"),
        ["FFF", " TS", " T "],
        {F: "minecraft:flint", S: "minecraft:string", T: "minecraft:stick"}
    )
    e.shaped(Item.of("minecraft:wooden_axe"),
        ["FS", "FT"],
        {F: "minecraft:flint", S: "minecraft:string", T: "minecraft:stick"}
    )
    e.shaped(Item.of("minecraft:wooden_hoe"),
        ["FF", "TS"],
        {F: "minecraft:flint", S: "minecraft:string", T: "minecraft:stick"}
    )
    e.shaped(Item.of("farmersdelight:flint_knife"),
        [" F", "TS"],
        {F: "minecraft:flint", S: "minecraft:string", T: "minecraft:stick"}
    )

    e.shaped(Item.of("minecraft:stone_axe"),
        ["NN ", "NTS", " T "],
        {N: "minecraft:smooth_stone", S: "minecraft:string", T: "minecraft:stick"}
    )
    e.shaped(Item.of("minecraft:stone_pickaxe"),
        ["NNN", " TS", " T "],
        {N: "minecraft:smooth_stone", S: "minecraft:string", T: "minecraft:stick"}
    )
    e.shaped(Item.of("minecraft:stone_shovel"),
        [" N ", " TS", " T "],
        {N: "minecraft:smooth_stone", S: "minecraft:string", T: "minecraft:stick"}
    )
    e.shaped(Item.of("minecraft:stone_hoe"),
        ["NN ", "ST ", " T "],
        {N: "minecraft:smooth_stone", S: "minecraft:string", T: "minecraft:stick"}
    )
    e.shaped(Item.of("minecraft:stone_sword"),
        [" N ", "TNT", " TS"],
        {N: "minecraft:smooth_stone", S: "minecraft:string", T: "minecraft:stick"}
    )

    function make_tool(tier, ingot, sheet) {
        e.shaped(Item.of("minecraft:"+tier+"_axe"),
            ["PI ", "PS ", "HS "],
            {P: sheet, I: ingot, S: "minecraft:stick", H: "#create:hammers"}
        )
        e.shaped(Item.of("minecraft:"+tier+"_pickaxe"),
            ["PII", "HS ", " S "],
            {P: sheet, I: ingot, S: "minecraft:stick", H: "#create:hammers"}
        )
        e.shaped(Item.of("minecraft:"+tier+"_shovel"),
            ["HP ", " S ", " S "],
            {P: sheet, I: ingot, S: "minecraft:stick", H: "#create:hammers"}
        )
        e.shaped(Item.of("minecraft:"+tier+"_hoe"),
            ["PP ", "HS ", " S "],
            {P: sheet, I: ingot, S: "minecraft:stick", H: "#create:hammers"}
        )
        e.shaped(Item.of("minecraft:"+tier+"_sword"),
            ["HP ", "SPS", " S "],
            {P: sheet, I: ingot, S: "minecraft:stick", H: "#create:hammers"}
        )
        e.shaped(Item.of("create_ironworks:"+tier+"_paxel"),
            ["PII", "PSH", " S "],
            {P: sheet, I: ingot, S: "minecraft:stick", H: "#create:hammers"}
        )
        e.shaped(Item.of("create_ironworks:"+tier+"_hammer"),
            ["II ", "IIS", "II "],
            {P: sheet, I: ingot, S: "minecraft:stick", H: "#create:hammers"}
        )
    }
    make_tool("iron", "minecraft:iron_ingot", "#c:iron_plates")
    make_tool("copper", "minecraft:copper_ingot", "#c:copper_plates")
    make_tool("bronze", "#c:bronze_ingots", "#c:bronze_plates")
    make_tool("brass", "#c:brass_ingots", "#c:brass_plates")
    make_tool("steel", "#c:steel_ingots", "#c:steel_plates")

    /* SMOOTH STONE */
    e.remove({id: "minecraft:smooth_stone"})
    e.remove({id: "create:fan_blasting/minecraft/smooth_stone"})
    e.blasting("minecraft:smooth_stone", "minecraft:stone")
    e.custom({
        type: "create:sandpaper_polishing",
        ingredients: [
            {
                item: "minecraft:atone"
            }
        ],
        results: [
            {
                item: "minecraft:smooth_stone"
            }
        ]
    })

    /* IRON ALLOY FURNACE */
    e.remove({id: "techreborn:crafting_table/machine/iron_furnace"})
    e.remove({id: "minecraft:brick"})
    e.remove({id: "create:fan_blasting/minecraft/brick"})
    e.replaceInput({id: "techreborn:crafting_table/machine/iron_alloy_furnace"},
        "techreborn:refined_iron_ingot", "#c:tin_ingots"
    )

    /* FURNACE */
    e.replaceInput({id: "minecraft:furnace"},
        "#minecraft:stone_tool_materials", "kubejs:firebricks"
    )
    e.shapeless(Item.of("2x kubejs:empty_form"),
        [
            "#c:tools/knives",
            "#minecraft:wooden_slabs"
        ]
    ).damageIngredient("#c:tools/knives", 2)
    e.shapeless(Item.of("kubejs:clay_form"),
        [
            "minecraft:clay",
            "kubejs:empty_form"
        ]
    )
    e.shapeless(Item.of("techreborn:clay_dust"),
        [
            "kubejs:mortar",
            "minecraft:clay"
        ]
    ).damageIngredient("kubejs:mortar")
    e.campfireCooking("minecraft:brick", "kubejs:clay_form", 0, 300)
    e.shapeless(Item.of("kubejs:brick_dust"),
        [
            "kubejs:mortar",
            "minecraft:brick"
        ]
    ).damageIngredient("kubejs:mortar")
    e.shapeless(Item.of("2x kubejs:firebrick_dust"),
        [
            "techreborn:clay_dust",
            "kubejs:brick_dust"
        ]
    )
    e.shapeless(Item.of("kubejs:firebrick_form"),
        [
            "kubejs:firebrick_dust",
            "kubejs:empty_form"
        ]
    )
    e.campfireCooking("kubejs:firebrick", "kubejs:firebrick_form", 0, 300)
    e.shaped(Item.of("kubejs:firebricks"),
        [
            "XX",
            "XX"
        ],
        {
            X: "kubejs:firebrick"
        }
    )
    e.shaped(Item.of("minecraft:furnace"),
        [
            "XXX",
            "X X",
            "XXX"
        ],
        {
            X: "kubejs:firebricks"
        }
    )
    /* ANDESITE ALLOY */
    e.shapeless(Item.of("techreborn:andesite_dust"),
        [
            "kubejs:mortar",
            "minecraft:andesite"
        ]
    ).damageIngredient("kubejs:mortar")
    e.custom({
        type: "techreborn:alloy_smelter",
        ingredients: [
            {
                item: "techreborn:andesite_dust"
            },
            {
                item: "minecraft:iron_nugget"
            }
        ],
        results: [
            {
                item: "create:andesite_alloy"
            }
        ],
        power: 6,
        time: 200
    })

    /* GLASS */
    e.remove({id: "minecraft:glass"})
    e.remove({id: "betterend:end_glass_smelting"})
    e.remove({id: "create:fan_blasting/minecraft/glass"})
    e.remove({id: "create:fan_blasting/betterend/end_glass_smelting"})
    e.shapeless(Item.of("kubejs:sand_dust"),
        [
            "kubejs:mortar",
            "minecraft:sand"
        ]
    ).damageIngredient("kubejs:mortar")
    e.shapeless(Item.of("techreborn:flint_dust"),
        [
            "kubejs:mortar",
            "minecraft:flint"
        ]
    ).damageIngredient("kubejs:mortar")
    e.shapeless(Item.of("8x kubejs:glass_dust"),
        [
            "kubejs:sand_dust",
            "kubejs:sand_dust",
            "kubejs:sand_dust",
            "kubejs:sand_dust",
            "kubejs:sand_dust",
            "kubejs:sand_dust",
            "kubejs:sand_dust",
            "kubejs:sand_dust",
            "techreborn:flint_dust"
        ]
    )
    e.campfireCooking("minecraft:glass", "kubejs:glass_dust", 0, 200)
    e.blasting("minecraft:glass", "kubejs:glass_dust", 0, 200)
    e.custom({
        type: "create:mixing",
        ingredients: [
            {item: "minecraft:sand"},
            {item: "minecraft:sand"},
            {item: "minecraft:sand"},
            {item: "minecraft:sand"},
            {item: "minecraft:sand"},
            {item: "minecraft:sand"},
            {item: "minecraft:sand"},
            {item: "minecraft:sand"},
            {item: "techreborn:flint_dust"},
        ],
        results: [
            {
                item: "kubejs:glass_dust",
                count: 8
            },
        ]
    })

    /* WOOD AND PLANKS */
    e.remove({input: "#minecraft:logs", output: "#minecraft:planks", type: "minecraft:crafting"})
    e.remove({id: "minecraft:stick"})
    e.shapeless(Item.of("4x minecraft:stick"),
        [
            "#c:tools/knives",
            "#minecraft:planks"
        ]
    ).damageIngredient("#c:tools/knives")
    for (const mod in global.wood) {
        for (const wood in global.wood[mod]) {
            e.shapeless(Item.of("4x "+mod+":"+wood+"_planks"),
                [
                    "#c:tools/knives",
                    "#"+mod+":"+wood+"_logs"
                ]
            ).damageIngredient("#c:tools/knives")
        }
    }
})
