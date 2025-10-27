// priority: 10

console.info('Hello, templates!')

global.item = {};
global.item.one = (id) => {return {item: id}};
global.item.item = (id, count) => {return {item: id, count: count}};
global.item.fluid = (id, amount) => {return {fluid: id, amount: amount}};
global.item.chance = (id, count, chance) => {return {item: id, count: count, chance: chance}};
global.item.tag = (tag, count) => {return {tag: tag, count: count}};

global.ad_astra = {}

global.ad_astra.alloying = (result, ingredients, cookingtime, energy) => {
	return {
	  type: "ad_astra:alloying",
	  cookingtime: cookingtime,
	  energy: energy,
	  ingredients: ingredients,
	  result: {
	    count: Item.of(result).getCount(),
	    id: Item.of(result).getId()
	  }
	}
}

global.ad_astra.cryofreezing = () => {} // TODO
global.ad_astra.nasa_workbench = () => {} // TODO

function create_grinding() {};
function create_crafting() {};
function create_wiremilling() {};
function create_blasting() {};
function create_washing() {};
function create_freezing() {};
function create_milling() {};
function create_mixing() {};
function create_pressing() {};

function techreborn_grinder() {};
function techreborn_compressor() {};
function techreborn_fusion_reactor() {};
function techreborn_assembler() {};
function techreborn_ind_grinder() {};
function techreborn_reactor() {};
function techreborn_() {};
