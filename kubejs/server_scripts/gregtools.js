// priority: 5

console.info('Hello, gregtools!')

const hammers = ["copper", "bronze", "brass", "steel", "iron", "gold", "diamond", "netherite"]
const mats = global.materials

ServerEvents.tags("item", e => {
    e.add("minecraft:smelts_to_glass", "betterend:endstone_dust")
    for (const mat of hammers) {
        e.add("create:hammers", "create_ironworks:"+mat+"_hammer")
    }
    const pickaxes = ["minecraft:wooden_pickaxe", "minecraft:stone_pickaxe", "minecraft:iron_pickaxe",
        "minecraft:golden_pickaxe", "minecraft:diamond_pickaxe", "minecraft:netherite_pickaxe",
        "create_ironworks:copper_pickaxe", "create_ironworks:bronze_pickaxe", "create_ironworks:brass_pickaxe",
        "create_ironworks:steel_pickaxe"
    ]
    for (const pick of pickaxes) {
        e.add("kubejs:pickaxes", pick)
    }
})

ServerEvents.recipes(e => {
    e.shaped(Item.of("kubejs:mortar"),
        [
            " T ",
            "STS",
            "SSS"
        ],
        {
            T: "#c:tin_ingots",
            S: "minecraft:smooth_stone"
        }
    )

    /* PLATES */
    /*for (const mat of mats) {
        if (!mat[global.PLATE]) {
            continue
        }
        e.shaped(
            Item.of(mat[global.PLATE]),
            [
                " H ",
                " P ",
                " P "
            ],
            {
                H: "#create:hammers",
                P: mat[global.INGOT]
            }
        )
    }*/
    /* DUSTS */

    /* WIRES */
})
