//priority: 10

const plates = ["create:sturdy_sheet", "create:copper_sheet", "create:brass_sheet", "create:iron_sheet", "create:golden_sheet", "create_dd:mithril_sheet", "create_dd:bronze_sheet", "create_dd:steel_sheet", "create_dd:industrial_iron_sheet", "create_dd:andesite_sheet", "create_dd:lapis_sheet", "create_dd:zinc_sheet", "create_dd:tin_sheet", "create_dd:shadow_steel_sheet", "create_dd:refined_radiance_sheet", "createaddition:zinc_sheet"]
const ingots = ["create:andesite_alloy", "create:zinc_ingot", "create:brass_ingot", "create_dd:mithril_ingot", "create_dd:bronze_ingot", "create_dd:steel_ingot", "create_dd:tin_ingot", "create_dd:industrial_iron_ingot", "create_dd:lapis_alloy", "create_dd:chromatic_compound", "create_dd:shadow_steel", "create_dd:refined_radiance", "createaddition:electrum_ingot", "minecraft:copper_ingot", "minecraft:gold_ingot", "minecraft:iron_ingot", "minecraft:netherite_ingot", "minecraft:brick", "betterend:thallasium_ingot", "minecraft:nether_brick"]

global.INGOT     = 0
global.BLOCK     = 1 // unused
global.NUGGET    = 2 // unused
global.PLATE     = 3
global.DUST      = 4
global.SMALLDUST = 5 // unused
global.ROD       = 6
global.WIRE      = 7
global.FINEWIRE  = 8 // unused
global.GEAR      = 9 // unused
global.ROTOR     = 10 // unused
global.HOTINGOT  = 11 // not completed
global.LIQUID    = 12 // not completed
global.MOLTEN    = 13 // not completed

global.materials = {
    iron: ["minecraft:iron_ingot", null, null, "create:iron_sheet", null, null, "ad_astra:iron_rod", "createaddition:iron_wire", null, null],
    industrial_iron: ["create_dd:industrial_iron_ingot", null, null, "create_dd:industrial_iron_sheet", null, null, null, null, null, null],
    copper: ["minecraft:copper_ingot", null, null, "create:copper_sheet", null, null, "createaddition:copper_rod", "createaddition:copper_wire", null, null],
    gold: ["minecraft:gold_ingot", null, null, "create:gold_sheet", null, null, "createaddition:gold_rod", "createaddition:gold_wire", null, null],
    andesite_alloy: ["create:andesite_alloy", null, null, "create_dd:andesite_sheet", null, null, null, null, null, null],
    steel: ["create_dd:steel_ingot", null, null, "create_dd:steel_sheet", "techreborn:steel_dust", null, "ad_astra:steel_rod", null, null, null],
    zinc: ["create:zinc_ingot", null, null, "create_dd:zinc_sheet", "techreborn:zinc_dust", null, null, null, null, null],
    brass: ["create:brass_ingot", null, null, "create:brass_sheet", "techreborn:brass_dust", null, "createaddition:brass_rod", null, null, null],
    bronze: ["create_dd:bronze_ingot", null, null, "create_dd:bronze_sheet", "techreborn:bronze_dust", null, null, null, null, null],
    tin: ["create_dd:tin_ingot", null, null, "create_dd:tin_sheet", null, null, null, null, null, null],
    electrum: ["createaddition:electrum_ingot", null, null, "createaddition:electrum_sheet", "techreborn:electrum_dust", null, "createaddition:electrum_rod", "createaddition:electrum_wire", null, null],
    andesite: ["minecraft:andesite", null, null, null, "techreborn:andesite_dust", null, null, null, null, null],
    diorite: ["minecraft:diorite", null, null, null, "techreborn:diorite_dust", null, null, null, null, null],
    granite: ["minecraft:granite", null, null, null, "techreborn:granite_dust", null, null, null, null, null],
    basalt: ["minecraft:basalt", null, null, null, "techreborn:basalt_dust", null, null, null, null, null],
    calcite: ["minecraft:calcite", null, null, null, "techreborn:calcite_dust", null, null, null, null, null],
    coal: ["minecraft:coal", null, null, null, "techreborn:coal_dust", null, null, null, null, null],
    charcoal: ["minecraft:charcoal", null, null, null, "techreborn:charcoal_dust", null, null, null, null, null],
    clay: ["minecraft:clay", null, null, null, "techreborn:clay_dust", null, null, null, null, null],
    flint: ["minecraft:flint", null, null, null, "techreborn:flint_dust", null, null, null, null, null],
    obsidian: ["minecraft:obsidian", null, null, null, "techreborn:obsidian", null, null, null, null, null],
    netherrack: ["minecraft:netherrack", null, null, null, "techreborn:netherrack_dust", null, null, null, null, null],
    quartz: ["minecraft:quartz", null, null, null, "techreborn:quartz_dust", null, null, null, null, null],

    certuz_quartz: ["ae2:certuz_quartz_crystal", null, null, null, "ae2:certuz_quartz_dust", null, null, null, null, null],
    fluix: ["ae2:fluix_crystal", null, null, null, "ae2:fluix_dust", null, null, null, null, null],
}

const mcmats = ["iron", "copper", "gold", "netherite"]
const admats = ["desh", "ostrum", "calorite", "steel", "iron", "etrium"]
const trmats = ["tin", "zinc", "refined_iron", "steel", "lead", "nickel", "bronze", "brass", "mixed_metal", "invar", "silver", "electrum", "aluminum", "titanium", "chrome", "iridium", "iridium_alloy", "tungsten", "tungstensteel"]

global.wood = {
    minecraft: ["oak", "spruce", "birch", "jungle", "acacia", "dark_oak", "mangrove", "cherry"],
    betterend: ["mossy_glowshroom", "pythadendron", "end_lotus", "lacugrove", "dragon_tree", "tenanea",
        "helix_tree", "umbrella_tree", "jellyshroom", "lucernia"],
    regions_unexplored: ["baobab", "blackwood", "blue_bioshroom", "brimwood", "cobalt", "cypress", "dead",
        "eucalyptus", "green_bioshroom", "joshua", "kapok", "larch", "magnolia", "maple", "mauve", "palm", "pine",
        "pink_bioshroom", "redwood", "socotra", "willow", "yellow_bioshroom"],
    techreborn: ["rubber"],
    create_dd: ["rubber"],
    ad_astra: ["glacian"]
}
