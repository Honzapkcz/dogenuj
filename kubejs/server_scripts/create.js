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

    /* RECIPES OF RESOURCES */
    //TODO: brass, bronze, industrial ingot, steel
    // alloying brass

    /* RECIPES OF BASIC THINGS */
    /* RECIPES OF MACHINES */
})
