// priority: 0

// Visit the wiki for more info - https://kubejs.com/

console.info('Hello, food!')

ItemEvents.modification(e => {
    e.modify("createbb:white_meth", item => {
        item.foodProperties = food => {
            food.alwaysEdible(true)
            food.effect("minecraft:poison", 20, 1, 0.25)
            food.effect("minecraft:darkness", 20, 1, 0.25)
            food.effect("minecraft:nausea", 20, 1, 0.25)
            food.effect("minecraft:mining_fatigue", 20, 1, 0.25)

            food.effect("minecraft:speed", 200, 2, 0.25)
            food.effect("minecraft:strength", 200, 2, 0.25)
            food.effect("minecraft:resistance", 200, 2, 0.25)
            food.effect("farmersdelight:comfort", 100, 1, 0.25)
        }
    })

    e.modify("createbb:blue_meth", item => {
        item.foodProperties = food => {
            food.alwaysEdible(true)
            food.effect("minecraft:poison", 20, 1, 0.25)
            food.effect("minecraft:darkness", 20, 1, 0.25)
            food.effect("minecraft:nausea", 20, 1, 0.25)
            food.effect("minecraft:mining_fatigue", 20, 1, 0.25)
            food.effect("create_bic_bit:unanchored", 20, 1, 0.25)
            food.effect("create_bic_bit:oiled_up", 20, 1, 0.25)

            food.effect("minecraft:speed", 200, 4, 0.25)
            food.effect("minecraft:strength", 200, 4, 0.25)
            food.effect("minecraft:resistance", 200, 3, 0.25)
            food.effect("farmersdelight:comfort", 100, 2, 0.25)
            food.effect("minecraft:haste", 200, 2, 0.25)
            food.effect("minecraft:night_vision", 200, 2, 0.25)
        }
    })

    e.modify("supplementaries:soap", item => {
        item.foodProperties = food => {
            food.alwaysEdible(true)
        }
    })
})
