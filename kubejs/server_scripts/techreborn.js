// priority: 0

console.info('Hello, techreborn!')

ServerEvents.recipes(e => {
    e.remove({id: "techreborn:crafting_table/tool/bronze_pickaxe"})
    e.remove({id: "techreborn:crafting_table/tool/bronze_spade"})
    e.remove({id: "techreborn:crafting_table/tool/bronze_sword"})
    e.remove({id: "techreborn:crafting_table/tool/bronze_axe"})
    e.remove({id: "techreborn:crafting_table/tool/bronze_hoe"})
    e.remove({id: "techreborn:crafting_table/armor/bronze_helmet"})
    e.remove({id: "techreborn:crafting_table/armor/bronze_chestplate"})
    e.remove({id: "techreborn:crafting_table/armor/bronze_boots"})
    e.remove({id: "techreborn:crafting_table/armor/bronze_leggings"})
    e.remove({id: "techreborn:crafting_table/armor/steel_helmet"})
    e.remove({id: "techreborn:crafting_table/armor/steel_chestplate"})
    e.remove({id: "techreborn:crafting_table/armor/steel_boots"})
    e.remove({id: "techreborn:crafting_table/armor/steel_leggings"})

    e.custom({
        type: "create:mechanical_crafting",
        acceptMirrored: false,
        pattern: [
            "STSTS",
            "THRHT",
            "SRIRS",
            "THRHT",
            "STSTS"
        ],
        key: {
            S: {item: "ad_astra:steel_plate"},
            T: {item: "minecraft:tnt"},
            H: {item: "techreborn:tritium_bucket"},
            R: {item: "create_new_age:radioactive_thorium"},
            I: {item: "techreborn:industrial_machine_frame"},
        },
        result: {
            item: "techreborn:nuke",
        }
    })
})