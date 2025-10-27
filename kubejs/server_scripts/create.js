// priority: 0

// Visit the wiki for more info - https://kubejs.com/

console.info('Hello, create!')

ServerEvents.recipes(e => {
    /* TOOL CONFLICTS */
    e.remove({id: "create_ironworks:tools/paxel/steel"})
    e.remove({id: "create_ironworks:tools/hoe/steel"})
    e.remove({id: "create_ironworks:tools/pickaxe/steel"})
    e.remove({id: "create_ironworks:tools/hammer/steel"})
    e.remove({id: "create_ironworks:tools/sword/steel"})
    e.remove({id: "create_ironworks:tools/shovel/steel"})
    e.remove({id: "create_ironworks:tools/axe/steel"})
    e.remove({id: "create_ironworks:armor/leggings/steel"})
    e.remove({id: "create_ironworks:armor/chestplate/steel"})
    e.remove({id: "create_ironworks:armor/helmet/steel"})
    e.remove({id: "create_ironworks:armor/boots/steel"})
    e.remove({id: "create_ironworks:tools/paxel/bronze"})
    e.remove({id: "create_ironworks:tools/hoe/bronze"})
    e.remove({id: "create_ironworks:tools/pickaxe/bronze"})
    e.remove({id: "create_ironworks:tools/hammer/bronze"})
    e.remove({id: "create_ironworks:tools/sword/bronze"})
    e.remove({id: "create_ironworks:tools/shovel/bronze"})
    e.remove({id: "create_ironworks:tools/axe/bronze"})
    e.remove({id: "create_ironworks:armor/leggings/bronze"})
    e.remove({id: "create_ironworks:armor/chestplate/bronze"})
    e.remove({id: "create_ironworks:armor/helmet/bronze"})
    e.remove({id: "create_ironworks:armor/boots/bronze"})

    e.remove({id: "createbigcannons:cutting/autocannon_cartridge_sheet_iron"})
    e.remove({id: "createbigcannons:cutting/autocannon_cartridge_sheet_gold"})
    e.remove({id: "createbigcannons:cutting/autocannon_cartridge_sheet_copper"})

    e.remove({id: "createdeco:pressing/andesite_sheet"})
    e.replaceInput({input: "createdeco:andesite_sheet"},
        "createdeco:andesite_sheet", "create_dd:andesite_sheet"
    )
	e.custom({
		type: "create:compacting",
		heatRequirement: "heated",
		ingredients: [
			{item: "minecraft:cobblestone", count: 2},
			{item: "minecraft:sand", count: 2}
		],
		results: [
			{item: "minecraft:end_stone"}
		]
	})

    /* RECIPES OF RESOURCES */
    //TODO: brass, bronze, industrial ingot, steel
    e.replaceInput({input: "#c:bronze_plates"}, "#c:bronze_plates", "create_dd:bronze_sheet")
    e.replaceInput({input: "#c:bronze_ingots"}, "#c:bronze_ingots", "crate_dd:bronze_ingot")
    e.replaceInput({input: "create_ironworks:bronze_ingot"}, "create_ironworks:bronze_ingot", "create_dd:bronze_ingot")
    e.replaceInput({input: "techreborn:bronze_ingot"}, "techreborn:bronze_ingot", "create_dd:bronze_ingot")
    //TODO: remove some recipes after brass merge
    
    // alloying brass

    /* KINEMATICS */
    e.remove({id: "create:crafting/kinetics/large_cogwheel"})
    e.remove({id: "create:crafting/kinetics/large_cogwheel_from_little"})
    e.remove({id: "create:crafting/kinetics/cogwheel"})
    e.remove({id: "create:crafting/kinetics/brass_hand"})
    e.remove({id: "create_dd:crafting/brass_hand"})
    e.shaped(Item.of("create:brass_hand"),
		[
			" A ",
			"BBB",
			" B "
		],
		{
			A: "create:andesite_alloy",
			B: "create_dd:bronze_sheet",
	})

	//e.replaceInput({id: "create:crafting_"})
    /* RECIPES OF MACHINES */
})
