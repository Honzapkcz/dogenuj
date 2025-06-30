// priority: 0

// Visit the wiki for more info - https://kubejs.com/

console.info('Hello, early_game!')


StartupEvents.registry("item", e => {
    e.create("padding")
    e.create("dirty_crushed_iron")
    e.create("dirty_crushed_tin")
    e.create("empty_form")
    e.create("clay_form")
    e.create("brick_dust")
    e.create("firebrick_dust")
    e.create("firebrick_form")
    e.create("firebrick")
    //e.create("sand_dust")
    //e.create("glass_dust")
})

StartupEvents.registry("block", e => {
    e.create("firebricks")
        .stoneSoundType()
        .hardness(3.0)
        .resistance(6.0)
        .fullBlock(true)
        .requiresTool(true)
})
// kubejs:padding
// kubejs:dirty_crushed_iron
// kubejs:dirty_crushed_tin
// kubejs:empty_form
// kubejs:clay_form
// kubejs:brick_dust
// kubejs:firebrick_dust
// kubejs:firebrick_form
// kubejs:firebrick
// kubejs:firebricks

// rename wooden tools to flint