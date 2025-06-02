// priority: 0

console.info('Hello, ae2!')

ServerEvents.recipes(e => {
    function for_cell(type, tier) {
        e.remove({id: "ae2:network/cells/"+type+"_storage_cell_"+tier+"k"})
        e.remove({id: "ae2:network/cells/"+type+"_storage_cell_"+tier+"k_storage"})
        e.custom({
            type: "techreborn:assembling_machine",
            power: 20,
            time: 200,
            ingredients: [
                {item: "ae2:"+type+"_cell_housing"},
                {item: "ae2:cell_component_"+tier+"k"}
            ],
            results: [
                {item: "ae2:"+type+"_storage_cell_"+tier+"k"}
            ]
        })
    }

    function for_spatial(tier) {
        e.remove({id: "ae2:network/cells/spatial_storage_cell_"+tier+"_cubed"})
        e.remove({id: "ae2:network/cells/spatial_storage_cell_"+tier+"_cubed_storage"})
        e.custom({
            type: "techreborn:assembling_machine",
            power: 20,
            time: 200,
            ingredients: [
                {item: "ae2:item_cell_housing"},
                {item: "ae2:spatial_cell_component_"+tier}
            ],
            results: [
                {item: "ae2:spatial_storage_cell_"+tier}
            ]
        })
    }

    e.remove({mod: "ae2", type: "create:automatic_packing"})
    e.remove({output: "ae2:silicon"})
    e.remove({input: "ae2:silicon"})

    e.replaceInput({}, "ae2:silicon", "techreborn:silicon_plate")

    e.custom({
        type: "ae2:inscriber",
        ingredients: {
            middle: {
                item: "techreborn:silicon_plate"
            },
            top: {
                item: "ae2:silicon_press"
            }
        },
        mode: "inscribe",
        result: {
            item: "ae2:printed_silicon"
            }
    })

    for_cell("item", 1)
    for_cell("item", 4)
    for_cell("item", 16)
    for_cell("item", 64)
    for_cell("item", 256)
    for_cell("fluid", 1)
    for_cell("fluid", 4)
    for_cell("fluid", 16)
    for_cell("fluid", 64)
    for_cell("fluid", 256)
    for_spatial(4)
    for_spatial(16)
    for_spatial(128)
})