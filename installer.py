#!/bin/python
import os
import requests
from shutil import rmtree
import zipfile

print("\033[32m█| █|█|  █|    █|█|  █|█|  █|    █|\033[0m")
print("\033[32m█|█| █|  █|    █|██| █|█|  █|    █|\033[0m")
print("\033[32m██|  █|  █|    █|█|█|█|█|  █|    █|\033[0m")
print("\033[32m█|█| █|  █|█|  █|█| ██|█|  █|█|  █|\033[0m")
print("\033[32m█| █|█████|█████|█|  █|█████|█████|\033[0m")
print("\033[32mMinecraft Kujnuj instalační skript \033[0m")
print("")

# TODO: scripts.zip -> kubejs.zip
# TODO: Content-Lenght progressbar
# TODO: modpack.json

version = "KUJNUJ 3.0.0"
useragent = {"User-Agent": "Kujnuj/3.0.0 (honzapkcz)"}
upstream = "https://hbmy.eu/modpack/"

mods = [
    # MODS #
    "https://cdn.modrinth.com/data/3ufwT9JF/versions/gZClwdxY/ad_astra-fabric-1.20.1-1.15.20.jar",
    "https://cdn.modrinth.com/data/CFX9ftUJ/versions/KLFf6PpA/advancednetherite-fabric-2.1.3-1.20.1.jar",
    "https://cdn.modrinth.com/data/EsAfCjCV/versions/xcauwnEB/appleskin-fabric-mc1.20.1-2.5.1.jar",
    "https://cdn.modrinth.com/data/td9zQQBq/versions/HFlEAPtz/archon-0.8.1.jar",
    "https://cdn.modrinth.com/data/DhSSvaxs/versions/6tIaagwA/beautify-1.2.0%2B1.20.1.jar",
    "https://cdn.modrinth.com/data/gJ5afkVv/versions/m0GUubvz/bellsandwhistles-0.4.5%2B1.20.1-FABRIC.jar",
    "https://cdn.modrinth.com/data/Q2OqKxDG/versions/g2QPj5Kb/BetterAdvancements-Fabric-1.20.1-0.4.2.25.jar",
    "https://cdn.modrinth.com/data/gc8OEnCC/versions/7QwyTILr/better-end-4.0.11.jar",
    "https://cdn.modrinth.com/data/8shC1gFX/versions/7WkFnw9F/BetterF3-7.0.2-Fabric-1.20.1.jar",
    "https://cdn.modrinth.com/data/dGVX5JbJ/versions/ZnQ5dQNb/bettervillage-fabric-1.20.1-3.3.1.jar",
    "https://cdn.modrinth.com/data/RWrgTm1s/versions/xid3xe06/better_farming_right_click-1.20.1-fabric-1.0.0.jar",
    "https://cdn.modrinth.com/data/G1s2WpNo/versions/1yJzEpzh/BetterThirdPerson-Fabric-1.20-1.9.0.jar",
    "https://cdn.modrinth.com/data/joEfVgkn/versions/Mkla4B3q/carryon-fabric-1.20.1-2.1.2.7.jar",
    "https://cdn.modrinth.com/data/gu7yAYhd/versions/ZNdfrsWY/cc-tweaked-1.20.1-fabric-1.116.2.jar",
    "https://cdn.modrinth.com/data/F0AMrDjl/versions/PnOeHKsf/classicperipherals-0.2.8-fabric-1.20.1.jar",
    "https://cdn.modrinth.com/data/Wb5oqrBJ/versions/LFbNBVoh/chat_heads-0.14.0-fabric-1.20.jar",
    "https://cdn.modrinth.com/data/BAscRYKm/versions/pwyEaKDs/chipped-fabric-1.20.1-3.0.7.jar",
    "https://cdn.modrinth.com/data/vPNqo58Q/versions/XydHmhny/clienttweaks-fabric-1.20.1-11.1.5.jar",
    "https://cdn.modrinth.com/data/Wnxd13zP/versions/hefSwtn6/Clumps-fabric-1.20.1-12.0.0.4.jar",
    "https://cdn.modrinth.com/data/1IjD5062/versions/qGTDcjHM/continuity-3.0.0%2B1.20.1.jar",
    "https://cdn.modrinth.com/data/iDyqnQLT/versions/Wbb5zXWc/coolrain-1.3.0-1.20.1.jar",
    "https://cdn.modrinth.com/data/UT2M39wf/versions/WYmjbo0H/copycats-2.2.2%2Bmc.1.20.1-fabric.jar",
    "https://cdn.modrinth.com/data/DMu0oBKf/versions/9y4MPSVS/craftingtweaks-fabric-1.20.1-18.2.6.jar",
    "https://cdn.modrinth.com/data/kU1G12Nn/versions/ybLiaryg/createaddition-fabric%2B1.20.1-1.2.6.jar",
    "https://cdn.modrinth.com/data/uIfluo9C/versions/5Ibh9a9W/createbb1.20.1.jar",
    "https://cdn.modrinth.com/data/Jdbbtt0i/versions/SJpLT0Bq/CreateNumismatics-1.0.15%2Bfabric-mc1.20.1.jar",
    "https://cdn.modrinth.com/data/16DuAG4k/versions/odRnaQxT/create_bitterballen-0.0.86%2B1.20.1-fabric.jar",
    "https://cdn.modrinth.com/data/ihpnEd80/versions/VEhxPD2J/createcobblestone-1.4.4%2Bfabric-1.20.1-95.jar",
    "https://cdn.modrinth.com/data/aqYNR6rI/versions/zuDV9GQp/create_copper_and_zinc-1.6.0-fabric-1.20.1.jar",
    "https://cdn.modrinth.com/data/OkZtwdmt/versions/pQ2UTLTN/create-dd-ore-veins-disabler-1.1.jar",
    "https://cdn.modrinth.com/data/JmybsfWs/versions/Knv9sBsR/create_dd-0.1d.jar",
    "https://cdn.modrinth.com/data/sMvUb4Rb/versions/GsxgfeNu/createdeco-2.0.2-1.20.1-fabric.jar",
    "https://cdn.modrinth.com/data/HrsF061q/versions/GWWkSXtF/create-deco-additions-1.3.jar",
    "https://cdn.modrinth.com/data/76TqKW7O/versions/Yve4E42b/create_deepfried-0.1.1B%2B1.20.1.jar",
    "https://cdn.modrinth.com/data/reiRz8zO/versions/cgeIYny5/createdieselgenerators-2.1.4.jar",
    "https://cdn.modrinth.com/data/AEZO385x/versions/SI0RzkGk/create_enchantment_industry-1.2.16.jar",
    "https://cdn.modrinth.com/data/Xbc0uyRg/versions/7Ub71nPb/create-fabric-0.5.1-j-build.1631%2Bmc1.20.1.jar",
    "https://cdn.modrinth.com/data/FTeXqI9v/versions/rk63oafd/create-new-age-fabric-1.20.1-1.1.2.jar",
    "https://cdn.modrinth.com/data/GWp4jCJj/versions/bIFKELd8/createbigcannons-5.8.2-mc.1.20.1-fabric.jar",
    "https://cdn.modrinth.com/data/PnhmwLM0/versions/5ddQZm9q/createorigins-1.4.2%2B1.20.1.jar",
    "https://cdn.modrinth.com/data/X9kjRZeX/versions/TtSEksvr/create_oxidized-0.1.1%2B1.20.1.jar",
    "https://cdn.modrinth.com/data/jUlR3XZM/versions/aqdJaQxc/Create_Questing-FABRIC-1.0.1.jar",
    "https://cdn.modrinth.com/data/Dq3STxps/versions/fXKmWm2r/createrailwaysnavigator-fabric-1.20.1-beta-0.8.4.jar",
    "https://cdn.modrinth.com/data/N9QToVpw/versions/rqKE4xS1/create_ultimate_factory-2.1.0-fabric-1.20.1.jar",
    "https://cdn.modrinth.com/data/GNxdLCoP/versions/3rzOQJrq/cullleaves-fabric-3.2.0.jar",
    "https://cdn.modrinth.com/data/MI1LWe93/versions/Mw0Hq1SZ/creeperoverhaul-3.0.2-fabric.jar",
    "https://cdn.modrinth.com/data/HSfsxuTo/versions/9vHj342y/Explorify%20v1.6.4%20f15-88.mod.jar",
    "https://cdn.modrinth.com/data/HhIJW8n1/versions/MCFB20q2/Estrogen-4.3.4%2B1.20.1-fabric.jar",
    "https://cdn.modrinth.com/data/NNAgCjsB/versions/WWoTbpsx/entityculling-fabric-1.9.3-mc1.20.1.jar",
    "https://cdn.modrinth.com/data/UVtY3ZAC/versions/LeAiyr1s/EnchantmentDescriptions-Fabric-1.20.1-17.1.19.jar",
    "https://cdn.modrinth.com/data/pZ2wrerK/versions/NFPdxMt9/emotecraft-for-MC1.20.1-2.2.7-b.build.50-fabric.jar",
    "https://cdn.modrinth.com/data/72GXx2MO/versions/ELIJcdMH/Emojiful-Fabric-1.20.1-4.2.0.jar",
    "https://cdn.modrinth.com/data/v3CYg2V9/versions/nIQb1yEH/drippyloadingscreen_fabric_3.0.12_MC_1.20.1.jar",
    "https://cdn.modrinth.com/data/tpehi7ww/versions/d1sY0JqV/dungeons-and-taverns-3.0.3.f.jar",
    "https://cdn.modrinth.com/data/6FtRfnLg/versions/CuLlUIYD/do_a_barrel_roll-fabric-3.6.1%2B1.20.1.jar",
    "https://cdn.modrinth.com/data/9BgYgXE4/versions/DgDhbN2s/disenchanting_table-merged-1.20.1-5.0.2.jar",
    "https://cdn.modrinth.com/data/Wq5SjeWM/versions/L92PEacB/fancymenu_fabric_3.7.0_MC_1.20.1.jar",
    "https://cdn.modrinth.com/data/z3TzcquW/versions/1SN7K6ZX/fastpaintings-1.20-1.2.7-fabric.jar",
    "https://cdn.modrinth.com/data/7vxePowz/versions/PB4pwRax/FarmersDelight-1.20.1-2.4.0%2Brefabricated.jar",
    "https://cdn.modrinth.com/data/DJ1ZClf3/versions/UdveVUc3/dynamic-light-0.3.jar",
    "https://cdn.modrinth.com/data/pvcsfne4/versions/hV0Pl3WP/chefs-delight-1.0.3-fabric-1.20.1.jar",
    "https://cdn.modrinth.com/data/pJmCFF0p/versions/NRw0CDAc/handcrafted-fabric-1.20.1-3.0.6.jar",
    "https://cdn.modrinth.com/data/eE2Db4YU/versions/Ts0TsDkW/immersive_armors-1.7.1%2B1.20.1-fabric.jar",
    "https://cdn.modrinth.com/data/eE2Db4YU/versions/Ts0TsDkW/immersive_armors-1.7.1%2B1.20.1-fabric.jar",
    "https://cdn.modrinth.com/data/6txNkua3/versions/KVUoxnR1/immersive_paintings-0.6.8%2B1.20.1-fabric.jar",
    "https://cdn.modrinth.com/data/uKjKoMsj/versions/o64NJE0v/ImmersiveThunder-1.20.1%2B1.2.2.jar",
    "https://cdn.modrinth.com/data/Orvt0mRa/versions/nQHYSjxO/indium-1.0.36%2Bmc1.20.1.jar",
    "https://cdn.modrinth.com/data/YL57xq9U/versions/s5eFLITc/iris-1.7.6%2Bmc1.20.1.jar",
    "https://cdn.modrinth.com/data/TbriQCWD/versions/3Q4qBNwT/GeckoLibIrisCompat-Fabric-1.0.0.jar",
    "https://cdn.modrinth.com/data/yn9u3ypm/versions/66RxRZcI/graves-3.0.3%2B1.20.1.jar",
    "https://cdn.modrinth.com/data/n2de3t2z/versions/gioHN8Aw/ironchests-5.0.2-fabric.jar",
    "https://cdn.modrinth.com/data/y9vDr4Th/versions/aJFclmrq/itemcollectors-1.1.11-fabric-mc1.20.2.jar",
    "https://cdn.modrinth.com/data/1KLyhGRz/versions/LoyNhXfF/item-filters-fabric-2001.1.0-build.53.jar",
    "https://cdn.modrinth.com/data/u6dRKJwZ/versions/9FYfyBM7/jei-1.20.1-fabric-15.20.0.118.jar",
    "https://cdn.modrinth.com/data/uEfK2CXF/versions/9HWvOVzO/JustEnoughResources-Fabric-1.20.1-1.4.0.247.jar",
    "https://cdn.modrinth.com/data/fQEb0iXm/versions/jiDwS0W1/krypton-0.2.3.jar",
    "https://cdn.modrinth.com/data/umyGl7zF/versions/kPLHkyoJ/kubejs-fabric-2001.6.5-build.16.jar",
    "https://cdn.modrinth.com/data/hvFnDODi/versions/0.1.3/lazydfu-0.1.3.jar",
    "https://cdn.modrinth.com/data/Eh11TaTm/versions/txZ8qKXK/letsdo-herbalbrews-fabric-1.0.12.jar",
    "https://cdn.modrinth.com/data/vE2FN5qn/versions/rOkgwJ12/letmedespawn-1.20.x-fabric-1.5.0.jar",
    "https://cdn.modrinth.com/data/yjvKidNM/versions/tiE781mZ/lighty-fabric-2.1.3%2B1.20.1.jar",
    "https://cdn.modrinth.com/data/gvQqBUqZ/versions/vuuAe7ZA/lithium-fabric-mc1.20.1-0.11.3.jar",
    "https://cdn.modrinth.com/data/EltpO5cN/versions/udi9KR9R/lootr-fabric-1.20-0.7.35.85.jar",
    "https://cdn.modrinth.com/data/GmwLse2I/versions/fkcqoGXg/mcw-fences-1.2.0-1.20.1fabric.jar",
    "https://cdn.modrinth.com/data/GURcjz8O/versions/GOwdtbfi/mcw-bridges-3.1.0-mc1.20.1fabric.jar",
    "https://cdn.modrinth.com/data/kNxa8z3e/versions/HU3H8NiB/mcw-doors-1.1.2-mc1.20.1fabric.jar",
    "https://cdn.modrinth.com/data/dtWC90iB/versions/7aTbV3Sq/mcw-furniture-3.3.0-mc1.20.1fabric.jar",
    "https://cdn.modrinth.com/data/w4an97C2/versions/zdA7bseh/mcw-lights-1.1.2-mc1.20.1fabric.jar",
    "https://cdn.modrinth.com/data/okE6QVAY/versions/CwHvP3Pz/mcw-paintings-1.0.5-1.20.1fabric.jar",
    "https://cdn.modrinth.com/data/VRLhWB91/versions/hwnmaZHh/mcw-mcwpaths-1.1.1-mc1.20.1fabric.jar",
    "https://cdn.modrinth.com/data/B8jaH3P1/versions/BMjP4VXn/mcw-roofs-2.3.2-mc1.20.1fabric.jar",
    "https://cdn.modrinth.com/data/iP3wH1ha/versions/XNlrOt9m/mcw-stairs-1.0.1-1.20.1fabric.jar",
    "https://cdn.modrinth.com/data/n2fvCDlM/versions/6FBIUQpW/mcw-trapdoors-1.1.4-mc1.20.1fabric.jar",
    "https://cdn.modrinth.com/data/C7I0BCni/versions/Pj6cgTuw/mcw-mcwwindows-2.4.1-mc1.20.1fabric.jar",
    "https://cdn.modrinth.com/data/ZNk5S5U6/versions/oGKLI8RF/megane-fabric-20.1.2.jar",
    "https://cdn.modrinth.com/data/rQszQPD2/versions/OFIAZVy7/ModernKeyBinding-Fabric-1.20-1.2.0.jar",
    "https://cdn.modrinth.com/data/mOgUt4GM/versions/lEkperf6/modmenu-7.2.2.jar",
    "https://cdn.modrinth.com/data/JiEhJ3WG/versions/o6yyhzgj/moremobvariants-fabric%2B1.20.1-1.3.1.jar",
    "https://cdn.modrinth.com/data/F8BQNPWX/versions/tx891fzz/naturalist-5.0pre3%2Bfabric-1.20.1.jar",
    "https://cdn.modrinth.com/data/KuNKN7d2/versions/erSJnRcq/noisium-fabric-2.3.0%2Bmc1.20-1.20.1.jar",
    "https://cdn.modrinth.com/data/MPCX6s5C/versions/pm5lGOZk/notenoughanimations-fabric-1.10.6-mc1.20.1.jar",
    "https://cdn.modrinth.com/data/yyfwBmX3/versions/Pr6nLwHz/NEG-FABRIC-1.19.4-r1.5.3.jar",
    "https://cdn.modrinth.com/data/c8eIXMRR/versions/CsPwh4SC/openmcskins-1.19.4-2.0.0b4.jar",
    "https://cdn.modrinth.com/data/T0alwZVT/versions/YsNh3WnN/originfur-1.0.10.jar",
    "https://cdn.modrinth.com/data/3BeIrqZR/versions/oT0CGnBQ/Origins-1.10.2%2Bmc.1.20.x.jar",
    "https://cdn.modrinth.com/data/FiDptjtR/versions/EnGfmh9y/Origins-Classes-1.20-1.7.0.jar",
    "https://cdn.modrinth.com/data/uXXizFIs/versions/unerR5MN/ferritecore-6.0.1-fabric.jar",
    "https://cdn.modrinth.com/data/7d6mfXL5/versions/SG4SxM1r/PacketAuth-FabricQuilt-1.6.4_1.20-1.20.1.jar",
    "https://cdn.modrinth.com/data/nU0bVIaL/versions/Muu5nGmj/Patchouli-1.20.1-84.1-FABRIC.jar",
    "https://cdn.modrinth.com/data/hsOK0gUP/versions/i5skoC6m/plushies-1.4.0-fabric.jar",
    "https://cdn.modrinth.com/data/5BPpCYUe/versions/V4loooES/certain_questing_additions-fabric-1.0.7%2Bmc1.20.1.jar",
    "https://cdn.modrinth.com/data/aDbO5Ehv/versions/E3EMSqDg/%20rottenflesh-to-leather_1-20-x.jar",
    "https://cdn.modrinth.com/data/PE656UHx/versions/s3WWrpay/simple-hud-enhanced%2B1.20-1.20.1-4.7.5.jar",
    "https://cdn.modrinth.com/data/GmjmRQ0A/versions/EzpVcwYV/sliceanddice-fabric-3.3.1.jar",
    "https://cdn.modrinth.com/data/AANobbMI/versions/OihdIimA/sodium-fabric-0.5.13%2Bmc1.20.1.jar",
    "https://cdn.modrinth.com/data/PtjYWJkn/versions/mDbF0LZT/sodium-extra-0.5.9%2Bmc1.20.1.jar",
    "https://cdn.modrinth.com/data/qyVF9oeo/versions/sCsWXt85/sound-physics-remastered-fabric-1.20.1-1.5.1.jar",
    "https://cdn.modrinth.com/data/ZzjhlDgM/versions/VFhdqLko/Steam_Rails-1.6.9%2Bfabric-mc1.20.1.jar",
    "https://cdn.modrinth.com/data/2fltysAl/versions/frXSmfj0/StrawStatues-v8.0.3-1.20.1-Fabric.jar",
    "https://cdn.modrinth.com/data/fFEIiSDQ/versions/RWLHsKXP/supplementaries-1.20-3.1.41-fabric.jar",
    "https://cdn.modrinth.com/data/Ypb9Mccf/versions/KuBxKLJ2/recipe-advancements-yeeter-1.0.jar",
    "https://cdn.modrinth.com/data/Bh37bMuy/versions/Rc9pkPug/reeses_sodium_options-1.7.2%2Bmc1.20.1-build.101.jar",
    "https://cdn.modrinth.com/data/lWDHr9jE/versions/EInFBe6X/tectonic-3.0.16-fabric-1.20.1.jar",
    "https://cdn.modrinth.com/data/8oi3bsk5/versions/WeYhEb5d/Terralith_1.20.x_v2.5.4.jar",
    "https://cdn.modrinth.com/data/7cFX55fD/versions/1.0.3/timeoutout-1.0.3%2B1.19.1.jar",
    "https://cdn.modrinth.com/data/rlloIFEV/versions/vZN3DxP2/travelersbackpack-fabric-1.20.1-9.1.42.jar",
    "https://cdn.modrinth.com/data/klXONLDA/versions/Ob1PnUNR/villagesandpillages-fabric-mc1.20.1-1.0.2.jar",
    "https://cdn.modrinth.com/data/XZNI4Cpy/versions/nvqkBIsD/toms_storage_fabric-1.20-1.7.1.jar",
    "https://cdn.modrinth.com/data/Gx7SDgwQ/versions/TQ1tPR5u/toms_storage_creatified-0.2.0.jar",
    "https://cdn.modrinth.com/data/abooMhox/versions/EQYmDYvI/treeharvester-1.20.1-9.1.jar",
    "https://cdn.modrinth.com/data/5aaWibi9/versions/AHxQGtuC/trinkets-3.7.2.jar",
    "https://cdn.modrinth.com/data/9eGKb6K1/versions/FA95tUXq/voicechat-fabric-1.20.1-2.6.6.jar",
    "https://cdn.modrinth.com/data/7b5VoITI/versions/DomkrNR2/whats-that-slot-fabric-1.3.4%2B1.20.1.jar",
    "https://cdn.modrinth.com/data/6AQIaxuO/versions/kK5C4nuW/wthit-1.20.1-fabric-8.19.1.jar",
    "https://cdn.modrinth.com/data/MrLyhFlg/versions/UF0TWBtq/your-reputation-0.2.5%2Bwthit.1.20.jar",
    "https://cdn.modrinth.com/data/Ua7DFN59/versions/lscV1N5k/YungsApi-1.20-Fabric-4.0.6.jar",
    "https://cdn.modrinth.com/data/XNlO7sBv/versions/1Z9HNWpj/YungsBetterDesertTemples-1.20-Fabric-3.0.3.jar",
    "https://cdn.modrinth.com/data/o1C1Dkj5/versions/nidyvq2m/YungsBetterDungeons-1.20-Fabric-4.0.4.jar",
    "https://cdn.modrinth.com/data/2BwBOmBQ/versions/qJTsmyiE/YungsBetterEndIsland-1.20-Fabric-2.0.6.jar",
    "https://cdn.modrinth.com/data/z9Ve58Ih/versions/6LPrzuB0/YungsBetterJungleTemples-1.20-Fabric-2.0.5.jar",
    "https://cdn.modrinth.com/data/HjmxVlSr/versions/qLnQnqXS/YungsBetterMineshafts-1.20-Fabric-4.0.4.jar",
    "https://cdn.modrinth.com/data/Z2mXHnxP/versions/FL88RLRu/YungsBetterNetherFortresses-1.20-Fabric-2.0.6.jar",
    "https://cdn.modrinth.com/data/3dT9sgt4/versions/4c00pjbt/YungsBetterOceanMonuments-1.20-Fabric-3.0.4.jar",
    "https://cdn.modrinth.com/data/kidLKymU/versions/yV6hn0bB/YungsBetterStrongholds-1.20-Fabric-4.0.3.jar",
    "https://cdn.modrinth.com/data/Ht4BfYp6/versions/hvfjXu8d/YungsBridges-1.20-Fabric-4.0.3.jar",
    "https://cdn.modrinth.com/data/cs7iGVq1/versions/8h469FpE/YungsCaveBiomes-1.20.1-Fabric-2.0.5.jar",
    "https://cdn.modrinth.com/data/ZYgyPyfq/versions/pfVTUz1L/YungsExtras-1.20-Fabric-4.0.3.jar",
    "https://cdn.modrinth.com/data/w7ThoJFB/versions/hWl13Hjr/Zoomify-2.14.6%2B1.20.1.jar",
    # CURSEFORGE #
    "https://mediafilez.forgecdn.net/files/6891/920/goblintraders-fabric-1.20.1-1.11.5.jar",
    "https://mediafilez.forgecdn.net/files/6402/485/ftb-xmod-compat-fabric-2.1.3.jar",
    "https://mediafilez.forgecdn.net/files/6807/422/ftb-library-fabric-2001.2.10.jar",
    "https://mediafilez.forgecdn.net/files/6829/211/ftb-quests-fabric-2001.4.14.jar",
    "https://mediafilez.forgecdn.net/files/6130/783/ftb-teams-fabric-2001.3.1.jar",
    "https://mediafilez.forgecdn.net/files/6459/673/create_tweaked_controllers-0.1.0%2B1.20.1%5B0.5.1j%5D.jar",
    "https://mediafilez.forgecdn.net/files/6788/256/TechReborn-5.8.14.jar",
    "https://mediafilez.forgecdn.net/files/6844/217/TechRebornJEI-20.1.8.jar",
    "https://mediafilez.forgecdn.net/files/5265/767/IndustrialReborn-1.20.1-1.3.1.jar",
    "https://mediafilez.forgecdn.net/files/7110/920/refurbished_furniture-fabric-1.20.1-1.0.20.jar",
    # LIBRARIES #
    "https://cdn.modrinth.com/data/P7dR8mSH/versions/UapVHwiP/fabric-api-0.92.6%2B1.20.1.jar",
    "https://cdn.modrinth.com/data/1eAoo2KR/versions/dvS5DjUA/yet_another_config_lib_v3-3.6.6%2B1.20.1-fabric.jar",
    "https://cdn.modrinth.com/data/9s6osm5g/versions/2xQdCMyG/cloth-config-11.1.136-fabric.jar",
    "https://cdn.modrinth.com/data/ccKDOlHs/versions/zyOBB7J4/owo-lib-0.11.2%2B1.20.jar",
]

resourcepacks = [
    "https://srv.hbmc.net/modpack/kujnuj/Better-Leaves-8.1-1.20+.zip",
    "https://srv.hbmc.net/modpack/kujnuj/Enhanced+Audio+Ambience+r1.zip",
    "https://srv.hbmc.net/modpack/kujnuj/Enhanced+Audio+r6.zip",
    "https://srv.hbmc.net/modpack/kujnuj/FA+All_Extensions-v1.4.zip",
    "https://srv.hbmc.net/modpack/kujnuj/FreshAnimations_v1.9.2.zip",
    "https://srv.hbmc.net/modpack/kujnuj/MandalasGUI+Dakmode_1.20.5.zip",
    "https://srv.hbmc.net/modpack/kujnuj/xali's enchanted books v0.13.0.zip",
]

shaderpacks = [
    "https://srv.hbmc.net/modpack/kujnuj/BSL_v8.2.09p1.zip",
    "https://srv.hbmc.net/modpack/kujnuj/ComplementaryReimagined_r5.2.2.zip",
    "https://srv.hbmc.net/modpack/kujnuj/ComplementaryUnbound_r5.2.2.zip"
]

toplevel = [
    "https://srv.hbmc.net/modpack/kujnuj/options.txt"
]

kubejs = "https://srv.hbmc.net/modpack/kujnuj/kubejs.zip"

config = "https://srv.hbmc.net/modpack/kujnuj/config.zip"

cwd = os.getcwd()
newest = requests.get(upstream+"latest.txt", headers=useragent).text.splitlines()[0]
modpack = "Žádný"
modcount = 0
if os.path.isdir("mods"):
    for thing in os.listdir("mods"):
        if thing.endswith(".jar"):
            modcount += 1
if os.path.exists(".VERSION"):
    f = open(".VERSION", "r")
    modpack = f.readline()
    f.close()
elif os.path.exists("INSTALACE.txt"):
    modpack = "KUJNUJ Manuální Instalace"
elif modcount > 0:
    modpack = "Neznámý"


def download(url, folder, i, count, partzip=False):
    file = os.path.basename(url)
    if partzip:
        file = ".part.zip"
    infostr = f"[{folder}] [{i} / {count}]"
    print(f"{infostr} Stahuji {os.path.basename(url)}")
    r = requests.get(url, headers=useragent)
    # size = int(r.headers.get("content-length"))
    # wrote = 0
    with open(file, "wb") as f:
        for chunk in r.iter_content(chunk_size=65535):
            f.write(chunk)
            # wrote += 65535
            # print("\r%s [%10s] %s %i%%" % (infostr, "#"*int(wrote/size*10), file, int(wrote/size*100)), end="", flush=True)

    # print(f"\r{infostr} Staženo {file}                         ", flush=True)


def fetch(array, folder):
    print(f"Otevírám složku {folder}")
    if not os.path.isdir(folder):
        os.mkdir(folder)
    oldpath = os.getcwd()
    os.chdir(folder)
    i = 1
    for item in array:
        file = os.path.basename(item)
        if os.path.exists(file):
            print(f"[{i} / {len(array)}] Přeskakuji {file}")
        else:
            download(item, folder, i, len(array))
        i += 1
    print(f"Opouštím složku {folder}")
    os.chdir(oldpath)


def extract(webpath, folder):
    download(webpath, folder, 1, 1, True)
    print(f"Rozbaluji do {folder}")
    # TODO
    if not zipfile.is_zipfile(".part.zip"):
        print(f"\033[31mSoubor {webpath} není zip soubor!\033[0m")
        os.remove(".part.zip")
        return
    with zipfile.ZipFile(".part.zip") as f:
        f.extractall(folder)
    os.remove(".part.zip")


def install():
    global modpack
    if modpack != "Žádný":
        print("\033[31mDetekován modpack. Ve složce máte módy, které mohou narušit fungování modpacku.\033[0m")
        print("\033[31mPřejete si přesto pokračovat? (Instalátor nebude pokoušet přepisovat soubory)\033[0m")
        yesno = input("[ano|ne] ")
        if yesno != "ano":
            print("Nic neprovedeno")
            return
    fetch(mods, "mods")
    fetch(resourcepacks, "resourcepacks")
    fetch(shaderpacks, "shaderpacks")
    extract(config, ".")
    extract(kubejs, ".")
    fetch(toplevel, ".")

    print("Vytvářím .VERSION soubor")
    with open(".VERSION", "w") as f:
        f.write(version)
        f.write("\n")
    modpack = version
    print(f"\033[32mModpack {version} úspěšně nainstalován!\033[0m")


def uninstall():
    global modpack
    print("\033[31mTato akce nejde vrátit zpět!\033[0m")
    print("\033[31mOpravdu si přejete nadobro vymazat všechny módy?\033[0m")
    if input("[ano|ne] ") == "ano":
        print("Maži mods")
        rmtree("mods")
        os.mkdir("mods")
        print("\033[31mChcete vymazat i configy?\033[0m")
        if input("[ano|ne] ") == "ano":
            print("Maži config")
            rmtree("config")
            os.mkdir("config")
            os.remove("options.txt")
        print("Maži verze soubor")
        if os.path.exists("INSTALACE.txt"):
            os.remove("INSTALACE.txt")
        if os.path.exists(".VERSION"):
            os.remove(".VERSION")
        modpack = "Žádný"
        print("Úspěšně vymazáno")
    else:
        print("Nic neprovedeno")


def diagnose():
    modcount = 0
    if os.path.isdir("mods"):
        for thing in os.listdir("mods"):
            if thing.endswith(".jar"):
                modcount += 1
    print("\033[32mVerze Skriptu: \033[0m"+str(version))
    print("\033[32mDetekovaný Modpack: \033[0m"+str(modpack))
    print("\033[32mNejnovější Verze: \033[0m"+str(newest))
    print("\033[32mInstalační Cesta: \033[0m"+str(cwd))
    print("\033[32mPočet modů v mods složce: \033[0m"+str(modcount))
    print("\033[32mPočet modů v modpacku: \033[0m"+str(len(mods)))
    print("\033[32mUpstream: \033[0m"+str(upstream))
    print("")
    # TODO
    if cwd != "*.minecraft":
        print("\033[31mTato složka není '.minecraft', ujistěte se, že jste skript opravdu spustili v minecraft složce\033[0m")

    if modpack != "Žádný":
        print("\033[31mDetekován modpack. Při instalaci je nutno tuto verzi nejprve odinstalovat.\033[0m")

    if version != newest:
        print("\033[32mDostupná nová verze \033[0m"+str(newest))


diagnose()
while True:
    print("")
    print("Dostupné akce:")
    print("    1 - Nainstalovat Modpack")
    print("    2 - Odinstalovat/Vyčistit Modpack")
    print("    3 - Diagnostika")
    print("    4 - Odejít")
    print("")
    usin = input("[Akce] ")
    print("")

    if usin == "1":
        install()
    elif usin == "2":
        uninstall()
    elif usin == "3":
        diagnose()
    elif usin == "4":
        print("\033[32m[Konec]\033[0m")
        break
