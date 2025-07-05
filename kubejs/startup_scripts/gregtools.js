// priority: 0

// Visit the wiki for more info - https://kubejs.com/

console.info('Hello, gregtools!')

StartupEvents.registry("item", e => {
    e.create("mortar", "sword")
        .unstackable()
        .maxDamage(128)
        .tooltip("For crushing earlygame resources")
        .displayName("Mortar")
        .tier("wood")
        .attackDamageBaseline(0.0)
        .attackDamageBonus(0.0)
        .speedBaseline(0.0)
        .speed(0.0)
})

ItemEvents.modification(e => {
    function crem(item) {
        e.modify(item, iitem => {
            iitem.craftingRemainder = Item.of(item).item
        })
    }

    const hammers = ["copper", "bronze", "brass", "steel", "iron", "gold", "diamond", "netherite"]
    const knives = ["flint", "iron", "diamond", "netherite", "golden"]
    const pickaxes = ["minecraft:wooden_pickaxe", "minecraft:stone_pickaxe", "minecraft:iron_pickaxe",
        "minecraft:golden_pickaxe", "minecraft:diamond_pickaxe", "minecraft:netherite_pickaxe",
        "create_ironworks:copper_pickaxe", "create_ironworks:bronze_pickaxe", "create_ironworks:brass_pickaxe",
        "create_ironworks:steel_pickaxe"
    ]
    for (const mat in hammers) {
        crem("create_ironworks:"+mat+"_hammer")
    }
    crem("kubejs:mortar")
    crem("refurbished_furniture:knife")
    for (const mat in knives) {
        crem("farmersdelight:"+mat+"knife")
    }
})

BlockEvents.modification(e => {
    function tool(block) {
        e.modify(block, bm => {
            bm.requiresTool = true
        })
    }
    console.info("no more easy wood for you!")
    for (const mod in global.wood) {
        for (const wood of global.wood[mod]) {
            console.info("requireTool: "+mod+":"+wood)
            tool(mod+":"+wood+"_log")
            tool(mod+":"+wood+"_stripped_log")
        }
    }
})
