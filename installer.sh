#!/bin/bash
echo -e "\e[32m█| █|█|  █|    █|█|  █|█|  █|    █|\e[0m"
echo -e "\e[32m█|█| █|  █|    █|██| █|█|  █|    █|\e[0m"
echo -e "\e[32m██|  █|  █|    █|█|█|█|█|  █|    █|\e[0m"
echo -e "\e[32m█|█| █|  █|█|  █|█| ██|█|  █|█|  █|\e[0m"
echo -e "\e[32m█| █|█████|█████|█|  █|█████|█████|\e[0m"
echo -e "\e[32mMinecraft Kujnuj instalační skript\e[0m"
echo ""

cd $(dirname "$0")


#TODO: finish modlist
#TODO: server-side mods
#TODO: config
#TODO: resource packs
#TODO: shader packs
#TODO: scripts
#.minecraft/
#	config/
#		!unzip wget
#	mods/
#		!wget modlist
#	resourcepacks/
#		!wget reslist
#	scripts/
#		!unzip wget
#	shaderpacks/
#		!wget shalist

version="KUJNUJ 2.3.1"
useragent="Kujnuj/2.3.1 (honzapkcz)"
upstream="https://srv.hbmc.net/MODPACKVERSION"
mods=(
	"https://cdn.modrinth.com/data/3ufwT9JF/versions/gZClwdxY/ad_astra-fabric-1.20.1-1.15.20.jar"
	"https://cdn.modrinth.com/data/CFX9ftUJ/versions/KLFf6PpA/advancednetherite-fabric-2.1.3-1.20.1.jar"
	"https://cdn.modrinth.com/data/Gi02250Z/versions/QM6nx1Sa/almanac-1.20.x-fabric-1.0.2.jar"
	"https://cdn.modrinth.com/data/7zlUOZvb/versions/g5kqTxNB/azurelib-fabric-1.20.1-2.0.41.jar"
	"https://cdn.modrinth.com/data/EsAfCjCV/versions/xcauwnEB/appleskin-fabric-mc1.20.1-2.5.1.jar"
	"https://cdn.modrinth.com/data/XxWD5pD3/versions/Fb70Efd1/appliedenergistics2-fabric-15.3.3.jar"
	"https://cdn.modrinth.com/data/lhGA9TYQ/versions/WbL7MStR/architectury-9.2.14-fabric.jar"
	"https://cdn.modrinth.com/data/b1ZV3DIJ/versions/mXJWSwbJ/athena-fabric-1.20.1-3.1.2.jar"
	"https://cdn.modrinth.com/data/ftdbN0KK/versions/JjLWLyDz/badpackets-fabric-0.4.3.jar"
	"https://cdn.modrinth.com/data/MBAkmtvl/versions/OLj7g6Pc/balm-fabric-1.20.1-7.3.18.jar"
	"https://cdn.modrinth.com/data/BgNRHReB/versions/TPC86Pyz/bclib-3.0.14.jar"
	"https://cdn.modrinth.com/data/RWrgTm1s/versions/xid3xe06/better_farming_right_click-1.20.1-fabric-1.0.0.jar"
	"https://cdn.modrinth.com/data/gc8OEnCC/versions/7QwyTILr/better-end-4.0.11.jar"
	"https://cdn.modrinth.com/data/G1s2WpNo/versions/1yJzEpzh/BetterThirdPerson-Fabric-1.20-1.9.0.jar"
	"https://cdn.modrinth.com/data/uy4Cnpcm/versions/CBnLZwRS/Bookshelf-Fabric-1.20.1-20.2.13.jar"
	"https://cdn.modrinth.com/data/2u6LRnMa/versions/f3ATcSfq/botarium-fabric-1.20.1-2.3.4.jar"
	"https://cdn.modrinth.com/data/joEfVgkn/versions/Mkla4B3q/carryon-fabric-1.20.1-2.1.2.7.jar"
	"https://cdn.modrinth.com/data/gu7yAYhd/versions/5DpvDFcX/cc-tweaked-1.20.1-fabric-1.115.1.jar"
	"https://cdn.modrinth.com/data/Wb5oqrBJ/versions/iPRNNpDI/chat_heads-0.13.13-fabric-1.20.jar"
	"https://cdn.modrinth.com/data/BAscRYKm/versions/pwyEaKDs/chipped-fabric-1.20.1-3.0.7.jar"
	"https://cdn.modrinth.com/data/IwCkru1D/versions/cdcYbTHt/cicada-lib-0.10.2%2B1.20.1.jar"
	"https://cdn.modrinth.com/data/84USeAvk/versions/EvNWNIMY/clockwork-1.20.1-0.1.16-fabric-b3b22e39fe.jar"
	"https://cdn.modrinth.com/data/Wnxd13zP/versions/hefSwtn6/Clumps-fabric-1.20.1-12.0.0.4.jar"
	"https://cdn.modrinth.com/data/e0M1UDsY/versions/35WC69l2/collective-1.20.1-7.94.jar"
	"https://cdn.modrinth.com/data/DMu0oBKf/versions/bss6C81q/craftingtweaks-fabric-1.20.1-18.2.5.jar"
	"https://cdn.modrinth.com/data/kU1G12Nn/versions/vV4bZmhm/createaddition-fabric%2B1.20.1-1.2.4.jar"
	"https://cdn.modrinth.com/data/Xbc0uyRg/versions/7Ub71nPb/create-fabric-0.5.1-j-build.1631%2Bmc1.20.1.jar"
	"https://cdn.modrinth.com/data/C90qpzXw/versions/ck2DBQl8/createairfabric-1.0%2B1.20.1-26.jar"
	"https://cdn.modrinth.com/data/gJ5afkVv/versions/m0GUubvz/bellsandwhistles-0.4.5%2B1.20.1-FABRIC.jar"
	"https://cdn.modrinth.com/data/JmybsfWs/versions/Knv9sBsR/create_dd-0.1d.jar"
	"https://cdn.modrinth.com/data/sMvUb4Rb/versions/GsxgfeNu/createdeco-2.0.2-1.20.1-fabric.jar"
	"https://cdn.modrinth.com/data/zMna5NU5/versions/D9kmcPoc/createdieselgenerators-fabric-restitched-rel4.jar"
	"https://cdn.modrinth.com/data/76TqKW7O/versions/Yve4E42b/create_deepfried-0.1.1B%2B1.20.1.jar"
	"https://cdn.modrinth.com/data/jUlR3XZM/versions/aqdJaQxc/Create_Questing-FABRIC-1.0.1.jar"
	"https://cdn.modrinth.com/data/FZb6dmQf/versions/xhZ8eenR/create_ironworks-3.5.0-fabric-1.20.1.jar"
	"https://cdn.modrinth.com/data/Dq3STxps/versions/BNIhuyhA/createrailwaysnavigator-fabric-1.20.1-beta-0.7.2.jar"
	"https://cdn.modrinth.com/data/GmjmRQ0A/versions/EzpVcwYV/sliceanddice-fabric-3.3.1.jar"
	"https://cdn.modrinth.com/data/16DuAG4k/versions/odRnaQxT/create_bitterballen-0.0.86%2B1.20.1-fabric.jar"
	"https://cdn.modrinth.com/data/uIfluo9C/versions/5Ibh9a9W/createbb1.20.1.jar"
	"https://cdn.modrinth.com/data/GWp4jCJj/versions/bIFKELd8/createbigcannons-5.8.2-mc.1.20.1-fabric.jar"
	"https://cdn.modrinth.com/data/aqYNR6rI/versions/zuDV9GQp/create_copper_and_zinc-1.6.0-fabric-1.20.1.jar"
	"https://cdn.modrinth.com/data/UT2M39wf/versions/ecJyY73Y/copycats-2.2.1%2Bmc.1.20.1-fabric.jar"
	"https://cdn.modrinth.com/data/5ZuwMbpk/versions/IjyXHt7J/molten_metals-1.20.1-0.1.4-fabric.jar"
	"https://cdn.modrinth.com/data/q5i9RTSJ/versions/fo004jZj/create-metalwork-1.20.1-1.0.10-fabric.jar"
	"https://cdn.modrinth.com/data/FTeXqI9v/versions/rk63oafd/create-new-age-fabric-1.20.1-1.1.2.jar"
	"https://cdn.modrinth.com/data/Jdbbtt0i/versions/vnV7qp9x/CreateNumismatics-1.0.11%2Bfabric-mc1.20.1.jar"
	"https://cdn.modrinth.com/data/X9kjRZeX/versions/TtSEksvr/create_oxidized-0.1.1%2B1.20.1.jar"
	"https://cdn.modrinth.com/data/ZzjhlDgM/versions/VFhdqLko/Steam_Rails-1.6.9%2Bfabric-mc1.20.1.jar"
	"https://cdn.modrinth.com/data/N9QToVpw/versions/ilaQZdXE/create_ultimate_factory-1.9.0-fabric-1.20.1.jar"
	"https://cdn.modrinth.com/data/AEZO385x/versions/SI0RzkGk/create_enchantment_industry-1.2.16.jar"
	"https://cdn.modrinth.com/data/MI1LWe93/versions/Mw0Hq1SZ/creeperoverhaul-3.0.2-fabric.jar"
	"https://cdn.modrinth.com/data/GNxdLCoP/versions/3rzOQJrq/cullleaves-fabric-3.2.0.jar"
	"https://cdn.modrinth.com/data/6FtRfnLg/versions/CuLlUIYD/do_a_barrel_roll-fabric-3.6.1%2B1.20.1.jar"
	"https://cdn.modrinth.com/data/v3CYg2V9/versions/m3VjrnDR/drippyloadingscreen_fabric_3.0.2_MC_1.20.1.jar"
	"https://cdn.modrinth.com/data/fRiHVvU7/versions/DXUtDziE/emi-1.1.20%2B1.20.1%2Bfabric.jar"
	"https://cdn.modrinth.com/data/j2HhbEE7/versions/kWMqVWTm/emitrades-fabric-1.2.1%2Bmc1.20.1.jar"
	"https://cdn.modrinth.com/data/qbbO7Jns/versions/qMVMQnTb/emi_loot-0.7.5%2B1.20.1%2Bfix1%2Bfabric.jar"
	"https://cdn.modrinth.com/data/bpRHnWUb/versions/V1QbMdYW/extra-mod-integrations-0.4.7%2B1.20.1.jar"
	"https://cdn.modrinth.com/data/wbWoo11W/versions/lb6uuVk3/emi_enchanting-0.1.2%2B1.20.1.jar"
	"https://cdn.modrinth.com/data/sG4TqDb8/versions/Gg0pscgP/emi_ores-1.2%2B1.20.1%2Bfabric.jar"
	"https://cdn.modrinth.com/data/72GXx2MO/versions/ELIJcdMH/Emojiful-Fabric-1.20.1-4.2.0.jar"
	"https://cdn.modrinth.com/data/UVtY3ZAC/versions/LeAiyr1s/EnchantmentDescriptions-Fabric-1.20.1-17.1.19.jar"
	"https://cdn.modrinth.com/data/NNAgCjsB/versions/zdOMtwS8/entityculling-fabric-1.7.3-mc1.20.1.jar"
	"https://cdn.modrinth.com/data/Ha28R6CL/versions/FayzGq0c/fabric-language-kotlin-1.12.1%2Bkotlin.2.0.20.jar"
	"https://cdn.modrinth.com/data/lzVo0Dll/versions/62DUD085/fabric-permissions-api-0.3.1.jar"
	"https://cdn.modrinth.com/data/P7dR8mSH/versions/SKPWumQf/fabric-api-0.92.3%2B1.20.1.jar"
	"https://cdn.modrinth.com/data/Wq5SjeWM/versions/3dDslDXq/fancymenu_fabric_3.2.3_MC_1.20.1.jar"
	"https://cdn.modrinth.com/data/7vxePowz/versions/ZnoPlYRz/FarmersDelight-1.20.1-2.3.0%2Brefabricated.jar"
	"https://cdn.modrinth.com/data/z3TzcquW/versions/1SN7K6ZX/fastpaintings-1.20-1.2.7-fabric.jar"
	"https://cdn.modrinth.com/data/uXXizFIs/versions/unerR5MN/ferritecore-6.0.1-fabric.jar"
	"https://cdn.modrinth.com/data/hYykXjDp/versions/kZSxVWz7/fzzy_config-0.6.5%2B1.20.1.jar"
	"https://cdn.modrinth.com/data/8BmcQJ2H/versions/DAY9559u/geckolib-fabric-1.20.1-4.7.jar"
	"https://cdn.modrinth.com/data/TbriQCWD/versions/3Q4qBNwT/GeckoLibIrisCompat-Fabric-1.0.0.jar"
	"https://cdn.modrinth.com/data/pJmCFF0p/versions/NRw0CDAc/handcrafted-fabric-1.20.1-3.0.6.jar"
	"https://cdn.modrinth.com/data/eE2Db4YU/versions/Waf0D48D/immersive_armors-1.6.1%2B1.20.1-fabric.jar"
	"https://cdn.modrinth.com/data/Orvt0mRa/versions/nQHYSjxO/indium-1.0.36%2Bmc1.20.1.jar"
	"https://cdn.modrinth.com/data/YL57xq9U/versions/s5eFLITc/iris-1.7.6%2Bmc1.20.1.jar"
	"https://cdn.modrinth.com/data/n2de3t2z/versions/gioHN8Aw/ironchests-5.0.2-fabric.jar"
	"https://cdn.modrinth.com/data/y9vDr4Th/versions/W2clu40G/itemcollectors-1.1.10-fabric-mc1.20.jar"
	"https://cdn.modrinth.com/data/1KLyhGRz/versions/LoyNhXfF/item-filters-fabric-2001.1.0-build.53.jar"
	"https://cdn.modrinth.com/data/nvQzSEkH/versions/oJx1UoWN/Jade-1.20-Fabric-11.12.3.jar"
	"https://cdn.modrinth.com/data/fThnVRli/versions/DSkzT8Ma/JadeAddons-1.20.1-Fabric-5.4.0.jar"
	"https://cdn.modrinth.com/data/IYY9Siz8/versions/vVYtBiuW/jamlib-0.6.1%2B1.20.x.jar"
	"https://cdn.modrinth.com/data/u6dRKJwZ/versions/KcsHvRrB/jei-1.20.1-fabric-15.20.0.106.jar"
	"https://cdn.modrinth.com/data/uEfK2CXF/versions/9HWvOVzO/JustEnoughResources-Fabric-1.20.1-1.4.0.247.jar"
	"https://cdn.modrinth.com/data/J81TRJWm/versions/RlBGFlWp/konkrete_fabric_1.8.1_MC_1.20.1.jar"
	"https://cdn.modrinth.com/data/fQEb0iXm/versions/jiDwS0W1/krypton-0.2.3.jar"
	"https://cdn.modrinth.com/data/hvFnDODi/versions/0.1.3/lazydfu-0.1.3.jar"
	"https://cdn.modrinth.com/data/vE2FN5qn/versions/i9GmX6sU/letmedespawn-1.20.x-fabric-1.4.4.jar"
	"https://cdn.modrinth.com/data/gvQqBUqZ/versions/vuuAe7ZA/lithium-fabric-mc1.20.1-0.11.3.jar"
	"https://cdn.modrinth.com/data/GURcjz8O/versions/RmsMXs3r/mcw-bridges-3.0.0-mc1.20.1fabric.jar"
	"https://cdn.modrinth.com/data/kNxa8z3e/versions/HU3H8NiB/mcw-doors-1.1.2-mc1.20.1fabric.jar"
	"https://cdn.modrinth.com/data/GmwLse2I/versions/NxAYnOkJ/mcw-fences-1.1.2-mc1.20.1fabric.jar"
	"https://cdn.modrinth.com/data/dtWC90iB/versions/7aTbV3Sq/mcw-furniture-3.3.0-mc1.20.1fabric.jar"
	"https://cdn.modrinth.com/data/rH20L2Lp/versions/UScUkprf/mcw-holidays-1.1.0-mc1.20.1fabric.jar"
	"https://cdn.modrinth.com/data/w4an97C2/versions/D8iZj41A/mcw-lights-1.1.1-mc1.20.1fabric.jar"
	"https://cdn.modrinth.com/data/okE6QVAY/versions/CwHvP3Pz/mcw-paintings-1.0.5-1.20.1fabric.jar"
	"https://cdn.modrinth.com/data/VRLhWB91/versions/fNu9PbhG/mcw-paths-1.1.0fabric-mc1.20.1.jar"
	"https://cdn.modrinth.com/data/B8jaH3P1/versions/EOjhPmTj/mcw-roofs-2.3.1-mc1.20.1fabric.jar"
	"https://cdn.modrinth.com/data/iP3wH1ha/versions/XNlrOt9m/mcw-stairs-1.0.1-1.20.1fabric.jar"
	"https://cdn.modrinth.com/data/n2fvCDlM/versions/6FBIUQpW/mcw-trapdoors-1.1.4-mc1.20.1fabric.jar"
	"https://cdn.modrinth.com/data/C7I0BCni/versions/88sYNcv4/mcw-windows-2.3.0-mc1.20.1fabric.jar"
	"https://cdn.modrinth.com/data/CVT4pFB2/versions/2o0oW8Yv/melody_fabric_1.0.4_MC_1.20.1-1.20.4.jar"
	"https://cdn.modrinth.com/data/Umsczw3y/versions/hjc0Imm7/mythiclib-1.1.0%2B1.20.1.jar"
	"https://cdn.modrinth.com/data/ERH7cFoy/versions/cD4zn9kb/mythicupgrades-4.2.0%2Bmc1.20.1.jar"
	"https://cdn.modrinth.com/data/mOgUt4GM/versions/lEkperf6/modmenu-7.2.2.jar"
	"https://cdn.modrinth.com/data/JiEhJ3WG/versions/o6yyhzgj/moremobvariants-fabric%2B1.20.1-1.3.1.jar"
	"https://cdn.modrinth.com/data/F8BQNPWX/versions/dMGBsRgz/naturalist-fabric-4.0.3-1.20.1.jar"
	"https://cdn.modrinth.com/data/P1Kv5EAO/versions/bgc6xYvl/Necronomicon-Fabric-1.6.0%2B1.20.1.jar"
	"https://cdn.modrinth.com/data/MPCX6s5C/versions/sXmCy47p/notenoughanimations-fabric-1.9.2-mc1.20.1.jar"
	"https://cdn.modrinth.com/data/FiDptjtR/versions/EnGfmh9y/Origins-Classes-1.20-1.7.0.jar"
	"https://cdn.modrinth.com/data/T0alwZVT/versions/YsNh3WnN/originfur-1.0.10.jar"
	"https://cdn.modrinth.com/data/3BeIrqZR/versions/OdNHB7Bh/Origins-1.20.1-1.10.0.jar"
	"https://cdn.modrinth.com/data/c8eIXMRR/versions/CsPwh4SC/openmcskins-1.19.4-2.0.0b4.jar"
	"https://cdn.modrinth.com/data/ccKDOlHs/versions/zyOBB7J4/owo-lib-0.11.2%2B1.20.jar"
	"https://cdn.modrinth.com/data/7d6mfXL5/versions/SG4SxM1r/PacketAuth-FabricQuilt-1.6.4_1.20-1.20.1.jar"
	"https://cdn.modrinth.com/data/nU0bVIaL/versions/Muu5nGmj/Patchouli-1.20.1-84.1-FABRIC.jar"
	"https://cdn.modrinth.com/data/hsOK0gUP/versions/i5skoC6m/plushies-1.4.0-fabric.jar"
	"https://cdn.modrinth.com/data/QAGBst4M/versions/6dQXvzl5/PuzzlesLib-v8.1.29-1.20.1-Fabric.jar"
	"https://cdn.modrinth.com/data/Ypb9Mccf/versions/KuBxKLJ2/recipe-advancements-yeeter-1.0.jar"
	"https://cdn.modrinth.com/data/Bh37bMuy/versions/Rc9pkPug/reeses_sodium_options-1.7.2%2Bmc1.20.1-build.101.jar"
	"https://cdn.modrinth.com/data/aDbO5Ehv/versions/E3EMSqDg/%20rottenflesh-to-leather_1-20-x.jar"
	"https://cdn.modrinth.com/data/Tkikq67H/versions/rhE8MT9Z/RegionsUnexploredFabric-0.5.6%2B1.20.1.jar"
	"https://cdn.modrinth.com/data/G1hIVOrD/versions/UOdaYbhh/resourcefullib-fabric-1.20.1-2.1.29.jar"
	"https://cdn.modrinth.com/data/M1953qlQ/versions/2gStMKhM/resourcefulconfig-fabric-1.20.1-2.1.3.jar"
	"https://cdn.modrinth.com/data/9eGKb6K1/versions/pPL5s4GQ/voicechat-fabric-1.20.1-2.5.28.jar"
	"https://cdn.modrinth.com/data/AANobbMI/versions/OihdIimA/sodium-fabric-0.5.13%2Bmc1.20.1.jar"
	"https://cdn.modrinth.com/data/PtjYWJkn/versions/I7ggF6B5/sodium-extra-0.5.4%2Bmc1.20.1-build.115.jar"
	"https://cdn.modrinth.com/data/2fltysAl/versions/frXSmfj0/StrawStatues-v8.0.3-1.20.1-Fabric.jar"
	"https://cdn.modrinth.com/data/LN9BxssP/versions/Ur02nrUT/supermartijn642configlib-1.1.8a-fabric-mc1.20.jar"
	"https://cdn.modrinth.com/data/rOUBggPv/versions/T4PXaNJw/supermartijn642corelib-1.1.18a-fabric-mc1.20.1.jar"
	"https://cdn.modrinth.com/data/kkmrDlKT/versions/FZV63yhg/TerraBlender-fabric-1.20.1-3.0.1.7.jar"
	"https://cdn.modrinth.com/data/rlloIFEV/versions/5eLDOgGZ/travelersbackpack-fabric-1.20.1-9.1.29.jar"
	"https://cdn.modrinth.com/data/abooMhox/versions/EQYmDYvI/treeharvester-1.20.1-9.1.jar"
	"https://cdn.modrinth.com/data/5aaWibi9/versions/AHxQGtuC/trinkets-3.7.2.jar"
	"https://cdn.modrinth.com/data/3Acxy864/versions/PX90nVpR/uranus-2.2.2-1.20.1-fabric.jar"
	"https://cdn.modrinth.com/data/V5ujR2yw/versions/wDYLclLS/valkyrienskies-120-2.3.0-beta.5.jar"
	"https://cdn.modrinth.com/data/qS1ot7R2/versions/aLmH2zHD/VMod-Fabric-1.20.1-0.1.3.jar"
	"https://cdn.modrinth.com/data/6AQIaxuO/versions/Zhq1AsyE/wthit-fabric-8.16.1.jar"
	"https://cdn.modrinth.com/data/ZNk5S5U6/versions/oGKLI8RF/megane-fabric-20.1.2.jar"
	"https://cdn.modrinth.com/data/MrLyhFlg/versions/UF0TWBtq/your-reputation-0.2.5%2Bwthit.1.20.jar"
	"https://cdn.modrinth.com/data/1bokaNcj/versions/sDUGXv1w/Xaeros_Minimap_25.1.0_Fabric_1.20.jar"
	"https://cdn.modrinth.com/data/NcUtCpym/versions/Fwao7ZwU/XaerosWorldMap_1.39.4_Fabric_1.20.jar"
	"https://cdn.modrinth.com/data/EnPUzSTg/versions/D1gwdzhr/XaeroPlus-2.26.3%2Bfabric-1.20.1-WM1.39.4-MM25.1.0.jar"
	"https://cdn.modrinth.com/data/T6oqPfxF/versions/hcThI3QG/XaeroZoomout-Fabric-1.20-1.1.0.jar"
	"https://cdn.modrinth.com/data/1eAoo2KR/versions/kkPxieHD/yet_another_config_lib_v3-3.6.3%2B1.20.1-fabric.jar"
	"https://cdn.modrinth.com/data/Ua7DFN59/versions/lscV1N5k/YungsApi-1.20-Fabric-4.0.6.jar"
	"https://cdn.modrinth.com/data/t5FRdP87/versions/lYpHN3iF/YungsBetterWitchHuts-1.20-Fabric-3.0.3.jar"
	"https://cdn.modrinth.com/data/HjmxVlSr/versions/qLnQnqXS/YungsBetterMineshafts-1.20-Fabric-4.0.4.jar"
	"https://cdn.modrinth.com/data/Z2mXHnxP/versions/FL88RLRu/YungsBetterNetherFortresses-1.20-Fabric-2.0.6.jar"
	"https://cdn.modrinth.com/data/XNlO7sBv/versions/1Z9HNWpj/YungsBetterDesertTemples-1.20-Fabric-3.0.3.jar"
	"https://cdn.modrinth.com/data/o1C1Dkj5/versions/nidyvq2m/YungsBetterDungeons-1.20-Fabric-4.0.4.jar"
	"https://cdn.modrinth.com/data/z9Ve58Ih/versions/6LPrzuB0/YungsBetterJungleTemples-1.20-Fabric-2.0.5.jar"
	"https://cdn.modrinth.com/data/3dT9sgt4/versions/4c00pjbt/YungsBetterOceanMonuments-1.20-Fabric-3.0.4.jar"
	"https://cdn.modrinth.com/data/kidLKymU/versions/yV6hn0bB/YungsBetterStrongholds-1.20-Fabric-4.0.3.jar"
	"https://cdn.modrinth.com/data/w7ThoJFB/versions/RW06GEHk/Zoomify-2.14.2%2B1.20.1.jar"
	"https://cdn.modrinth.com/data/qyVF9oeo/versions/hxEab3Tk/sound-physics-remastered-fabric-1.20.1-1.4.8.jar"
	"https://cdn.modrinth.com/data/Nv2fQJo5/versions/2VRL4210/replaymod-1.20.1-2.6.20.jar"
	"https://cdn.modrinth.com/data/7cFX55fD/versions/1.0.3/timeoutout-1.0.3%2B1.19.1.jar"
	"https://cdn.modrinth.com/data/iM50gcBD/versions/JapPN4QV/windchimes-1.2.4%2B1.20.jar"
	"https://cdn.modrinth.com/data/uKjKoMsj/versions/o64NJE0v/ImmersiveThunder-1.20.1%2B1.2.2.jar"
	"https://cdn.modrinth.com/data/iDyqnQLT/versions/YEnuoMXW/coolrain-1.1.0-1.20.1.jar"
	"https://cdn.modrinth.com/data/6t2MdNbo/versions/deQpTLVc/alcocraftplus-1.20.1-fabric-2.0.2.jar"
	"https://cdn.modrinth.com/data/9BgYgXE4/versions/RQNYBT7T/disenchanting_table-merged-1.20.1-4.0.2.jar"
	"https://cdn.modrinth.com/data/rQszQPD2/versions/OFIAZVy7/ModernKeyBinding-Fabric-1.20-1.2.0.jar"
	"https://cdn.modrinth.com/data/PnhmwLM0/versions/5ddQZm9q/createorigins-1.4.2%2B1.20.1.jar"
	"https://cdn.modrinth.com/data/1IjD5062/versions/qGTDcjHM/continuity-3.0.0%2B1.20.1.jar"
	"https://cdn.modrinth.com/data/pZ2wrerK/versions/NFPdxMt9/emotecraft-for-MC1.20.1-2.2.7-b.build.50-fabric.jar"
	"https://cdn.modrinth.com/data/705gWllI/versions/BslzSzGd/emiffect-fabric-1.1.2%2Bmc1.20.1.jar"
	"https://cdn.modrinth.com/data/8shC1gFX/versions/7WkFnw9F/BetterF3-7.0.2-Fabric-1.20.1.jar"
	"https://cdn.modrinth.com/data/DhSSvaxs/versions/6tIaagwA/beautify-1.2.0%2B1.20.1.jar"
	"https://cdn.modrinth.com/data/EltpO5cN/versions/udi9KR9R/lootr-fabric-1.20-0.7.35.85.jar"
	"https://cdn.modrinth.com/data/6txNkua3/versions/UjL11A4h/immersive_paintings-0.6.7%2B1.20.1-fabric.jar"
	"https://cdn.modrinth.com/data/wnEe9KBa/versions/sV8lIBhJ/vmp-fabric-mc1.20.1-0.2.0%2Bbeta.7.102-all.jar"
	"https://cdn.modrinth.com/data/KuNKN7d2/versions/erSJnRcq/noisium-fabric-2.3.0%2Bmc1.20-1.20.1.jar"
	"https://cdn.modrinth.com/data/8ooWzSQP/versions/G74msHHs/spell_power-0.12.0%2B1.20.1.jar"
	"https://cdn.modrinth.com/data/td9zQQBq/versions/FhLMTovJ/archon-0.8.0.jar"
	"https://cdn.modrinth.com/data/vPNqo58Q/versions/qOrKqP96/clienttweaks-fabric-1.20.1-11.1.3.jar"
	"https://cdn.modrinth.com/data/MBAkmtvl/versions/UqThQVCU/balm-fabric-1.20.1-7.3.27.jar"
	"https://cdn.modrinth.com/data/kzwxhsjp/versions/dHimNl5m/accurate-block-placement-1.2.1.jar"
	"https://cdn.modrinth.com/data/aC3cM3Vq/versions/mjuG4AYd/MouseTweaks-fabric-mc1.20-2.26.jar"
	"https://cdn.modrinth.com/data/PE656UHx/versions/s3WWrpay/simple-hud-enhanced%2B1.20-1.20.1-4.7.5.jar"
	"https://cdn.modrinth.com/data/7b5VoITI/versions/DomkrNR2/whats-that-slot-fabric-1.3.4%2B1.20.1.jar"
	"https://cdn.modrinth.com/data/9leXt4A5/versions/iZGUey6l/monolib-fabric-1.20.1-2.0.0.jar"
	"https://cdn.modrinth.com/data/HhIJW8n1/versions/MCFB20q2/Estrogen-4.3.4%2B1.20.1-fabric.jar"
	"https://cdn.modrinth.com/data/ihpnEd80/versions/VEhxPD2J/createcobblestone-1.4.4%2Bfabric-1.20.1-95.jar"
	"https://cdn.modrinth.com/data/HhIJW8n1/versions/MCFB20q2/Estrogen-4.3.4%2B1.20.1-fabric.jar"
	"https://cdn.modrinth.com/data/umyGl7zF/versions/kPLHkyoJ/kubejs-fabric-2001.6.5-build.16.jar"
	"https://cdn.modrinth.com/data/sk9knFPE/versions/MLIu0Tct/rhino-fabric-2001.2.3-build.10.jar"
	"https://cdn.modrinth.com/data/fFEIiSDQ/versions/R5P1cLjK/supplementaries-1.20-2.8.10-fabric.jar"
	"https://cdn.modrinth.com/data/6iTJugQR/versions/ZhpB8HCZ/amendments-1.20-1.1.31-fabric.jar"
	"https://cdn.modrinth.com/data/twkfQtEc/versions/X5QZyeHj/moonlight-1.20-2.11.29-fabric.jar"
	"https://mediafilez.forgecdn.net/files/6210/177/betterchunkloading-fabric-1.20.1-5.4.jar"
	"https://mediafilez.forgecdn.net/files/5470/34/cupboard-fabric-1.20.1-2.7.jar"
	"https://mediafilez.forgecdn.net/files/5911/975/framework-fabric-1.20.1-0.7.12.jar"
	"https://mediafilez.forgecdn.net/files/6164/52/ftb-library-fabric-2001.2.9.jar"
	"https://mediafilez.forgecdn.net/files/6259/627/ftb-quests-fabric-2001.4.12.jar"
	"https://mediafilez.forgecdn.net/files/6130/783/ftb-teams-fabric-2001.3.1.jar"
	"https://mediafilez.forgecdn.net/files/6046/19/ftb-xmod-compat-fabric-2.1.2.jar"
	"https://mediafilez.forgecdn.net/files/4802/504/goblintraders-fabric-1.20.1-1.9.3.jar"
	"https://mediafilez.forgecdn.net/files/6272/883/refurbished_furniture-fabric-1.20.1-1.0.12.jar"
	"https://mediafilez.forgecdn.net/files/6168/112/TechReborn-5.8.8.jar"
	"https://mediafilez.forgecdn.net/files/4768/646/OriginsOrbRework-1.20.1-2.0.0-FABRIC.jar"
	"https://mediafilez.forgecdn.net/files/5698/979/questsadditions-fabric-1.20.1-1.4.6.jar"
	"https://mediafilez.forgecdn.net/files/4756/458/ragnagoblin-fabric-1.20.1-2.1.0.jar"
	"https://mediafilez.forgecdn.net/files/4573/177/light-overlay-8.0.0.jar"
	"https://mediafilez.forgecdn.net/files/5621/847/kubejs-create-fabric-2024.8.12-build.1.jar"
	"https://mediafilez.forgecdn.net/files/5706/124/graves-3.0.3%2B1.20.1.jar"
)
#"https://cdn.modrinth.com/data/MyfCcqiE/versions/YT1Sriuq/create_interactive-1.1.1-beta.3_1.20.1-fabric.jar"

#SERVER "https://cdn.modrinth.com/data/rkN8aqci/versions/xXhZI4u3/async-locator-fabric-1.20-1.3.0.jar"
#SERVER "https://cdn.modrinth.com/data/7LEWYKTV/versions/oe5KEgWu/RecipeCooldown-1.0.0.jar"
#SERVER "https://github.com/Zhincore/dynmap-trains/releases/download/v1.3/trains.js"
#SERVER "https://cdn.modrinth.com/data/LVN9ygNV/versions/pOxgWfwI/ledger-1.2.8.jar"
#SERVER DYNMAP
#SERVER DYNMAP-BLOCK-SCAN
#SERVER GOTTA-GO-FAST
#SERVER CREATE-TRACK-MAP
#SERVER WHERE-ARE-THEY

resourcepacks=(
	"https://srv.hbmc.net/modpack/kujnuj/Better-Leaves-8.1-1.20+.zip"
	"https://srv.hbmc.net/modpack/kujnuj/Enhanced+Audio+Ambience+r1.zip"
	"https://srv.hbmc.net/modpack/kujnuj/Enhanced+Audio+r6.zip"
	"https://srv.hbmc.net/modpack/kujnuj/FA+All_Extensions-v1.4.zip"
	"https://srv.hbmc.net/modpack/kujnuj/FreshAnimations_v1.9.2.zip"
	"https://srv.hbmc.net/modpack/kujnuj/MandalasGUI+Dakmode_1.20.5.zip"
	"https://srv.hbmc.net/modpack/kujnuj/xali's enchanted books v0.13.0.zip"
)

shaderpacks=(
	"https://srv.hbmc.net/modpack/kujnuj/BSL_v8.2.09p1.zip"
	"https://srv.hbmc.net/modpack/kujnuj/ComplementaryReimagined_r5.2.2.zip"
	"https://srv.hbmc.net/modpack/kujnuj/ComplementaryUnbound_r5.2.2.zip"
)

scripts="https://srv.hbmc.net/modpack/kujnuj/kubejs.tar.gz"

configs="https://srv.hbmc.net/modpack/kujnuj/config.tar.gz"

cwd=$(pwd)
newest=$(curl -s $upstream)
modpack="Žádný"
if [ -f ".VERSION" ]; then
	modpack=$(cat .VERSION)
elif [ -f "INSTALACE.txt" ]; then
	modpack="KUJNUJ Manuální Instalace"
elif [ $(find mods -maxdepth 1 -name "*.jar" 2> /dev/null | wc -l) -gt 0 ]; then
	modpack="Neznámý"
fi

function fetch-files {
	arrname=$1[@]
	arr=("${!arrname}")
	folder=$2
	echo "Otevírám složku $folder"
	mkdir -p $folder
	oldpath=$(pwd)
	cd $folder
	wget -nc -q --show-progress --user-agent="$useragent" "${arr[@]}"
	echo "Opouštím složku $folder"
	cd "$oldpath"
}

function extract-files {
	webpath=$1
	folder=$2
	echo "Stahuji $webpath"
	wget -q --show-progress -O ".extracted.tar.gz" "$webpath"
	echo "Rozbaluji do $folder"
	# eXtract Keep Verbose File
	tar -xkvf ".extracted.tar.gz"
	rm ".extracted.tar.gz"
}

function install-modpack {
	if [ "$modpack" != "Žádný" ]; then
		echo -e "\e[31mDetekován modpack. Ve složce máte módy, které mohou narušit fungování modpacku.\e[0m"
		echo -e "\e[31mPřejete si přesto pokračovat? (Instalátor nebude pokoušet přepisovat soubory)\e[0m"
		echo -n "[ano/ne] "
		read yesno
		if [ $yesno != "ano" ]; then
			echo "Nic neprovedeno"
			return
		fi
	fi
	# MODPACK INSTALACE POD

	fetch-files mods "mods"
	fetch-files resourcepacks "resourcepacks"
	fetch-files shaderpacks "shaderpacks"
	extract-files $configs "configs"
	extract-files $scripts "kubejs"
	wget -nc -q --show-progress --user-agent="$useragent" "https://srv.hbmc.net/modpack/kujnuj/options.txt"

	# MODPACK INSTALACE NAD
	echo "Vytvářím .VERSION soubor"
	echo "$version" > ".VERSION"
	modpack=$version
	echo -e "\e[32mModpack $version úspěšně nainstalován!\e[0m"
}

function uninstall-modpack {
	echo -e "\e[31mTato akce nejde vrátit zpět!\e[0m"
	echo -e "\e[31mOpravdu si přejete nadobro vymazat všechny módy?\e[0m"
	echo -n "[ano/ne] "
	read yesno
	if [ "$yesno" = "ano" ]; then
		# MODPACK UNINSTALACE HERE
		echo "Maži mods"
		rm -rf mods
		echo -e "\e[31mChcete vymazat i configy?\e[0m"
		echo -n "[ano/ne] "
		read yesno
		if [ "$yesno" = "ano" ]; then
			echo "Maži config"
			rm -rf config
			rm -rf options.txt
		else
			echo "Přeskakuji config"
		fi
		echo "Maži instrukce"
		rm -f INSTALACE.txt
		rm -f .VERSION
		# MODPACK UNINSTALACE HERE
		modpack="Žádný"
		echo -e "\e[32mÚspěšně vymazáno\e[0m"
	else
		echo "Nic neprovedeno"
	fi
}

function diagnose {
	echo -ne "\e[32mVerze Skriptu: \e[0m"
	echo $version
	echo -ne "\e[32mDetekovaný Modpack: \e[0m"
	echo $modpack
	echo -ne "\e[32mNejnovější Verze: \e[0m"
	echo $newest
	echo -ne "\e[32mInstalační Cesta: \e[0m"
	echo $cwd
	if $1; then
		echo -ne "\e[32mPočet modů v mods složce: \e[0m"
		echo $(find mods -maxdepth 1 -name "*.jar" 2> /dev/null | wc -l)
		echo -ne "\e[32mPočet modů v modpacku: \e[0m"
		echo ${#mods[@]}
		echo -ne "\e[32mUpstream: \e[0m"
		echo $upstream
	fi
	echo ""
	if [ $(basename $cwd) != ".minecraft" ]; then
		echo -e "\e[31mTato složka není '.minecraft', ujistěte se, že jste skript opravdu spustili v minecraft složce.\e[0m"
	fi
	if [ "$modpack" != "Žádný" ]; then
		echo -e "\e[33mDetekován modpack. Při instalaci je nutno tuto verzi nejprve odinstalovat.\e[0m"
	fi
	if [ "$version" != "$newest" ]; then
		echo -e "\e[33mDostupná nová verze $newest!\e[0m"
	fi
}

diagnose $(false)
alive=$(true)
while $alive; do
	echo ""
	echo "Dostupné akce:"
	echo "    1 - Nainstalovat Modpack"
	echo "    2 - Odinstalovat/Vyčistit Modpack"
	echo "    3 - Diagnostika"
	echo "    4 - Odejít"
	echo ""
	echo -n "[Akce] "
	read userinput
	echo ""

	case $userinput in
		("1")
			install-modpack
		;;
		("2")
			uninstall-modpack
		;;
		("3")
			diagnose $(true)
		;;
		("4")
			alive=$(false)
			echo "[Konec]"
			exit
		;;
	esac
done
