// priority: 0

console.info('Hello, Dogenuj+!')

ServerEvents.recipes(e => {
    e.shaped(
        Item.of("mcwwindows:bamboo_shutter", 1),
        [
            "BB ",
            "BB ",
            "BB "
        ],
        {
            B: "minecraft:bamboo"
        }
    )
    e.shaped(
        Item.of("handcrafted:wood_plate", 3),
        [
            "SSS",
            " S ",
            "   "
        ],
        {
            S: "#minecraft:wooden_slabs"
        }
    )
    e.remove({id: "minecraft:stonecutter"})
    e.remove({id: "minecraft:piston"})
    e.remove({id: "minecraft:rail"})
    e.remove({id: "minecraft:smithing_table"})
    e.remove({id: "minecraft:compass"})
    e.remove({id: "minecraft:minecart"})
    e.remove({id: "minecraft:piston"})
    e.remove({id: "minecraft:shulker_box"})
    e.remove({id: "minecraft:cauldron"})
    e.remove({id: "minecraft:shield"})
    e.remove({id: "minecraft:hopper"})
    e.remove({id: "minecraft:bucket"})

    e.remove({id: "betterend:end_stone_brick_cracked_wall"})
    e.remove({id: "betterend:end_stone_brick_weathered_wall"})
    e.remove({id: "regions_unexplored:blackstone_cluster"})
    e.remove({id: "regions_unexplored:yellow_dye_from_tall_yellow_bioshroom"})
    e.remove({id: "minecraft:tnt"})
    e.remove({id: "supplementaries:awnings/awning_dark_gray"})
    e.remove({id: "handcrafted:white_sheet"})

    e.remove({id: "betterend:bolux_mushroom_campfire"})
    e.remove({id: "betterend:end_berry_campfire"})
    e.remove({id: "betterend:end_fish_campfire"})
    e.remove({id: "betterend:chorus_mushroom_campfire"})
    e.remove({id: "naturalist:cooked_egg_from_campfire_cooking"})
    e.remove({id: "minecraft:cake"})
    e.remove({id: "naturalist:cake"})
    e.remove({id: "naturalist:cooked_egg"})
    e.remove({id: "naturalist:cooked_egg_from_smoking"})

    // mythic upgrades
    const mythicingots = [
        "topaz", "sapphire", "peridot", "aquamarine",
        "ametrine", "jade", "ruby",
    ]
    for (var ingot in mythicingots) {
        e.remove({id: "mythicupgrades:"+ingot+"_pickaxe_smithing"})
        e.remove({id: "mythicupgrades:"+ingot+"_axe_smithing"})
        e.remove({id: "mythicupgrades:"+ingot+"_hoe_smithing"})
        e.remove({id: "mythicupgrades:"+ingot+"_shovel_smithing"})
        e.remove({id: "mythicupgrades:"+ingot+"_sword_smithing"})
        e.remove({id: "mythicupgrades:"+ingot+"_leggings_smithing"})
        e.remove({id: "mythicupgrades:"+ingot+"_chestplate_smithing"})
        e.remove({id: "mythicupgrades:"+ingot+"_helmet_smithing"})
        e.remove({id: "mythicupgrades:"+ingot+"_boots_smithing"})
    }
    e.remove({id: "mythicupgrades:necoium_ingot_from_raw_necoium"})

    // mcw furnitures
    const treetypes = [
        "cherry", "mangrove", "acacia", "oak", "spruce", "birch",
        "jungle", "dark_oak", "crimson", "warped",
    ]
    for (var tree in treetypes) {
        e.remove({id: "mcwfurnitures:"+tree+"_covered_desk"})
        e.remove({id: "mcwfurnitures:stripped_"+tree+"_covered_desk"})
    }
    e.remove({id: "mcwholidays:bell_wall_deco_2"})
    
    //steeel
    e.remove({id: "create_dd:compacting/steel_ingot"})

    e.remove({id: "create_ironworks:materials/alloys/from_crushed/mixing_steel_from_charcoal"})
    e.remove({id: "create_ironworks:materials/alloys/from_crushed/mixing_steel_from_coal"})
    e.remove({id: "create_ironworks:materials/alloys/from_ingots/mixing_steel_from_charcoal"})
    e.remove({id: "create_ironworks:materials/alloys/from_ingots/mixing_steel_from_coal"})

    e.remove({id: "create:pressing/desh_plate"})
    e.remove({id: "create:pressing/calorite_plate"})
    e.remove({id: "create:pressing/steel_plate"})
    e.remove({id: "create:pressing/ostrum_plate"})

    e.remove({id: "techreborn:compressing/desh_plate"})
    e.remove({id: "techreborn:compressing/calorite_plate"})
    e.remove({id: "techreborn:compressing/steel_plate"})
    e.remove({id: "techreborn:compressing/ostrum_plate"})

    e.remove({id: "techreborn:compressing/desh_plate_from_block"})
    e.remove({id: "techreborn:compressing/calorite_plate_from_block"})
    e.remove({id: "techreborn:compressing/steel_plate_from_block"})
    e.remove({id: "techreborn:compressing/ostrum_plate_from_block"})

    e.remove({mod: "createdeco", type: "create:automatic_packing"})
    e.remove({id: "techreborn:crafting_table/machine/chunk_loader"})

    function replaceAll(what, replacer) {
        e.replaceInput({input: what}, what, replacer)
        e.replaceOutput({output: what}, what, replacer)
    }

    replaceAll("create_ironworks:steel_ingot", "ad_astra:steel_ingot")
    replaceAll("create_dd:steel_ingot", "ad_astra:steel_ingot")
    replaceAll("techreborn:steel_ingot", "ad_astra:steel_ingot")
})