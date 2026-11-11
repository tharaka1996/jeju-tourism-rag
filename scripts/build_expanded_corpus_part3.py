"""
Corpus Expansion Script Part 3 for Jeju Tourism RAG Assistant.
Covers History, Folk Culture, Forests, Museums, Olle Trails, and Markets (Documents 38 to 60).
"""

from pathlib import Path

DOCS_DIR = Path(__file__).resolve().parent.parent / "data" / "documents"
DOCS_DIR.mkdir(parents=True, exist_ok=True)

DOCUMENTS = {}

# ==============================================================================
# CATEGORY 6: CULTURAL HERITAGE & FOLK ARCHITECTURE (38 - 43)
# ==============================================================================

DOCUMENTS["38_jeju_haenyeo_unesco_intangible_heritage.txt"] = """Title: Jeju Haenyeo Diving Culture and UNESCO Intangible Heritage
Source: Jeju Haenyeo Museum & Cultural Heritage Administration
Access Date: 2026-10-20
Category: UNESCO Intangible Cultural Heritage & Maritime Culture

Overview:
The Haenyeo of Jeju Island are female divers who harvest marine life—such as sea cucumbers, abalone, conch, top shells, and sea mustard—from the ocean floor without using any underwater breathing apparatus or oxygen tanks. In December 2016, the "Culture of Jeju Haenyeo" was officially inscribed on the UNESCO Representative List of the Intangible Cultural Heritage of Humanity, recognizing its eco-friendly sustainable harvesting methods, female community solidarity, and indigenous shamanic rituals.

Key Cultural Practices and Traditions:
1. Muljil (Diving Technique) and Soombisori:
   - Haenyeo dive down to depths of 10 to 20 meters, holding their breath for 1 to 2 minutes at a time in frigid waters.
   - When emerging to the surface, they exhale and inhale through pursed lips, releasing a high-pitched, whistled sigh called "Soombisori", which expels accumulated carbon dioxide and oxygenates the blood.
2. Traditional Gear:
   - Mul-ot: Traditional white cotton diving garments used historically, now replaced by modern black neoprene wetsuits.
   - Taewak and Mangsari: A floating dried gourd (or modern styrofoam buoy) with an attached mesh net where harvested seafood is deposited.
   - Bitchang: A specialized metal chisel used to pry stubbornly attached abalone from deep underwater crevices.
3. Bulteok (Communal Stone Enclosures):
   - Circular basalt stone windbreaks built along rocky shorelines with an open fire pit in the center. Here divers changed into diving clothes, warmed their cold bodies between dives, discussed village fishery rules, and made democratic communal decisions.
4. Haenyeo Museum (Hado-ri, Gujwa-eup):
   - An extensive memorial museum showcasing authentic artifacts, traditional thatched seaside dwellings, oral life histories, and historical resistance against Japanese colonial exploitation. Admission: 1,100 KRW for adults.

Seasonal Harvesting Rules and Sustainability:
- Self-Imposed Marine Conservation: Strict prohibitions on harvesting immature abalone (under 7cm) or diving during spawning seasons to prevent overfishing.
"""

DOCUMENTS["39_samseonghyeol_and_tamna_kingdom_mythology.txt"] = """Title: Samseonghyeol and the Mythological Origins of Tamna
Source: Samseonghyeol Foundation & Jeju City Cultural Heritage Division
Access Date: 2026-10-20
Category: Historic Site & Island Mythology

Overview:
Located in Ido-dong, downtown Jeju City, Samseonghyeol ("Three Sacred Caves / Holes") is revered as the birthplace of the ancient Tamna Kingdom and the mythological origins of the Jeju people. Designated as Historic Site No. 134, this sacred forested shrine preserves three natural depressions in the earth where, according to founding mythology, the three ancestral demi-gods of Jeju emerged from the ground thousands of years ago.

The Founding Legend (Samseong Shinwha):
- The Three Demi-Gods: Long ago, the island was wild and uninhabited. From three sacred holes in the earth emerged three divine men: Go Eul-na, Yang Eul-na, and Bu Eul-na.
- Arrival of the Three Princesses: One day, a wooden chest washed ashore on the eastern coast (Yeonhonpo, near Seongsan) containing three beautiful princesses from the Eastern Kingdom of Byeoknang, along with boxes of grain seeds (rice, barley, millet) and calves, foals, and hunting hounds.
- Foundation of the Clans: The three demi-gods married the princesses. To divide their territory fairly, each prince shot an arrow from a central hill; where the arrows landed determined their ancestral clan estates (the First, Second, and Third Domains), establishing agriculture, animal husbandry, and the founding dynasties of the Tamna Kingdom (the modern Go, Yang, and Bu family clans of Korea).

Key Shrine Features and Visitor Experience:
- The Sacred Holes (Hyeol): The three earthen depressions are surrounded by a barrier of ancient, twisting pine trees that appear to bow reverently toward the sacred ground. Remarkably, snow never accumulates inside the holes during winter.
- Samsongjeon Shrine: The ancestral ceremonial hall where spring and autumn memorial sacrifices are conducted in traditional Joseon robes.
- Exhibition Hall & 3D Cinema: Displays ancient court records, royal seals, and a 14-minute animated documentary detailing the founding myth in English, Korean, Japanese, and Chinese.

Visitor Information:
- Operating Hours: Daily 09:00 to 18:00 (last admission 17:30). Open year-round.
- Admission Fees: Adults: 4,000 KRW; Youth/Military: 2,500 KRW; Children: 1,500 KRW; Seniors (65+): 1,500 KRW.
- Transportation: Centrally located near Jeju Folk Natural History Museum and Gwangyang rotary. Take City Bus 311, 312, 325, or 351 to "Samseonghyeol" stop.
"""

DOCUMENTS["40_jeju_mokgwana_and_gwandeokjeong_pavilion.txt"] = """Title: Jeju Mokgwana and Gwandeokjeong Historical Complex
Source: Jeju World Heritage Office & Cultural Heritage Administration
Access Date: 2026-10-20
Category: Historic Site & Joseon Architecture

Overview:
Situated in Samdo-dong in the historic core of Jeju City, Jeju Mokgwana was the provincial government headquarters (Mokgwana) from the Tamna Kingdom through the Joseon Dynasty (1392-1910). Fronting the complex stands Gwandeokjeong Pavilion (National Treasure No. 322), the oldest existing wooden structure on Jeju Island, constructed in 1448 by Jeju Magistrate Sin Suk-cheong as a training pavilion for civil defense and archery.

Key Architectural Structures and Cultural History:
1. Gwandeokjeong Pavilion (Treasure No. 322):
   - A single-story wooden pavilion with a majestic hip-and-gable roof resting on sturdy stone plinths.
   - The interior wooden beams feature exquisite 15th-century historical murals depicting scenes of hunting, naval battles, and Daoist immortals painted by early Joseon artists.
   - In front of the pavilion stand ancient stone grandfather statues (Dolhareubang), which originally guarded the fortress gates of Jeju Castle.
2. Restored Government Buildings:
   - Honghwagwan (banquet and reception hall for visiting royal envoys).
   - Yeonheegak (the primary office and study of the provincial magistrate).
   - Gyulimdang (the mandarin orange orchard pavilion, where magistrates composed poetry surrounded by fragrant citrus blossoms).
   - Manggyeolru (a two-story watchtower historically used to scan the northern ocean for invading Japanese pirate fleets).

Cultural Programs and Evening Openings:
- Night Opening Tours: During spring and autumn (May to October), Jeju Mokgwana opens for enchanting illuminated night tours (free entry from 18:00 to 21:30), hosting traditional musical concerts, shadow puppetry, and night lantern displays.
- Traditional Court Attire: Visitors can rent authentic Joseon dynasty hanbok and magistrate uniforms on-site for photography.
- Admission: Daytime entry: Adults 1,500 KRW; Youth 800 KRW; Children 400 KRW. Free entry for visitors wearing traditional Hanbok.

Transportation:
- Located in downtown Jeju City, a 10-minute walk from Dongmun Market and Chilseong-ro shopping street. Take City Bus 316, 325, 365, or 465 to "Gwandeokjeong" stop.
"""

DOCUMENTS["41_seongeup_folk_village_living_heritage.txt"] = """Title: Seongeup Folk Village Living Cultural Heritage Guide
Source: Cultural Heritage Administration & Pyoseon-myeon Office
Access Date: 2026-10-20
Category: Living Folk Village & Traditional Architecture

Overview:
Located at the foot of Hallasan in Pyoseon-myeon, Seongeup Folk Village (Important Folklore Cultural Heritage No. 188) was the administrative capital of the Jeongui County (Jeongui-hyeon) for over 500 years from 1423 until 1914. Unlike modern reconstructed museum villages, Seongeup is a genuine, living historical community where generations of local villagers continue to reside inside original thatched-roof stone homes and preserve traditional Jeju customs, dialects, and culinary heritage.

Unique Architectural and Folk Features:
1. Volcanic Thatch-Roof Architecture (Choga):
   - Low-profile basalt stone houses built with thick earthen mud and volcanic mortar, capped with dense golden thatch.
   - Straw Rope Netting (Jip-jul): The thatch is bound securely by heavy crisscrossing straw ropes tied to exterior stone brackets, preventing ferocious typhoon winds from stripping roofs away.
2. The Olle and Jeongnang Gate System:
   - Curved entrance alleyways (Olle) paved with volcanic stones that deflect prevailing coastal gales.
   - Traditional Three-Pole Gates (Jeongnang): Rather than wooden doors, farm entrances feature two stone pillars with three horizontal wooden poles (Jeongmok):
     - All 3 poles inserted: "Owner is far away traveling, return another day."
     - 2 poles inserted: "Owner is working in fields, returning this evening."
     - 1 pole inserted: "Owner is nearby in neighborhood, returning soon."
     - 0 poles inserted: "Owner is home, please enter."
3. Centenarian Zelkova and Hackberry Trees (Natural Monument No. 161):
   - Magnificent ancient trees standing over 600 years old guard the village center alongside the historic stone fortress walls and Jeongui-hyanggyo (Confucian County Academy).

Local Food and Drink Heritage:
- Omegit-tteok: Traditional dark green rice cakes made from glutinous millet flour, coated in whole boiled red beans.
- Omegisul: Authentic indigenous liquor brewed from fermented millet and nuruk yeast; smooth, sweet, and lightly sparkling.

Visitor Details:
- Admission: Free public entry 24/7.
- Local village docents provide free guided heritage walks departing from the village square.
- Transportation: Take Blue Trunk Bus 221 from Jeju Intercity Bus Terminal to "Seongeup Folk Village" (approx. 50 minutes).
"""

DOCUMENTS["42_jeju_folk_village_pyoseon.txt"] = """Title: Jeju Folk Village (Pyoseon) Comprehensive Museum Guide
Source: Jeju Folk Village Foundation & Pyoseon Tourism Department
Access Date: 2026-10-20
Category: Open-Air Ethnographic Museum & Folk Culture

Overview:
Spanning over 150,000 square meters directly adjacent to Pyoseon Beach, Jeju Folk Village is South Korea's premier comprehensive open-air ethnographic museum. It accurately preserves and displays the authentic lifestyle, architecture, spiritual beliefs, and agricultural tools of Jeju Island during the late Joseon Dynasty (specifically the 1890s).

Layout and Thematic Zones:
The village painstakingly dismantled, relocated, and reconstructed over 100 authentic traditional houses from across the island, organized into specialized thematic zones:
1. Mountain Village (Sangan-chon): Thatch dwellings of woodcutters and charcoal burners nestled in dense oak groves, showing wild boar traps and medicinal herb drying sheds.
2. Middle-Mountain Village (Jungsangan-chon): Homes of livestock ranchers and millet farmers, featuring cattle mills, stone granaries (Godeul-gae), and horse breeding stables.
3. Fishing Village (Eochon): Coastal dwellings of Haenyeo divers and fisherman, showcasing fishing net repair decks, boat anchors, and salt production pans.
4. Shamanic Shrines (Dang): Sacred village shrines dedicated to the 18,000 native gods of Jeju folklore, decorated with colorful silk strips and offerings.
5. Joseon Government Office and Exile House: Demonstrating the legal trials, penal instruments, and exile living quarters of court scholars banished to the island.

Cultural Experiences and Performances:
- Live Folk Performances: Daily presentations of traditional Jeju folk music, drumming, and farmers' dances (Nongak) at 11:30, 13:30, and 15:30.
- Hands-on Workshops: Millet cake making, natural persimmon dye fabric coloring (Gal-ot), traditional pottery shaping, and calligraphy stamping.
- Filming Location: Primary shooting site for the globally acclaimed historical television drama "Dae Jang Geum" (Jewel in the Palace).

Visiting Information, Fees, and Hours:
- Operating Hours: Daily 08:30 to 18:00 (summer until 18:30, winter until 17:00).
- Admission Fees: Adults (ages 19-64): 15,000 KRW; Seniors (65+): 13,000 KRW; Youth: 12,000 KRW; Children: 11,000 KRW.
- Tram Service: A traditional audio-guided mini-tram operates through the expansive grounds for visitors with limited mobility (1,000 KRW).

Transportation:
- Take Red Express Bus 121 from Jeju Airport directly to "Jeju Folk Village" stop (approx. 65 minutes).
"""

DOCUMENTS["43_hangpaduri_hangmong_historic_site.txt"] = """Title: Hangpaduri Hangmong Historic Site (Anti-Mongol Fortress)
Source: Cultural Heritage Administration & Aewol-eup Municipal Council
Access Date: 2026-10-20
Category: Historical Fortress & Military Heritage

Overview:
Hangpaduri Hangmong Historic Site (Historic Site No. 396) is located in Giseong-ri, Aewol-eup. It preserves the earthen defensive fortress and military headquarters of the Sambyeolcho ("Three Elite Patrols"), an elite military corps of the Goryeo Dynasty that waged a heroic, last-ditch war of resistance against the invading Mongol Empire (Yuan Dynasty) between 1271 and 1273.

Historical Significance and the Sambyeolcho Resistance:
- Anti-Mongol Defense: After the Goryeo court surrendered to the Mongols on the mainland, General Kim Tong-jeong led the patriotic Sambyeolcho army across the sea to Jeju Island.
- Double-Walled Fortress: To resist the impending combined Mongol-Goryeo invasion fleet, the Sambyeolcho constructed an inner stone fortress (circumference 800m) and an immense outer earthen rampart (Totseong, spanning 6 km) along the hill contours.
- Tragic Fall: In April 1273, a joint Mongol-Goryeo armada of 160 warships and 12,000 troops attacked the island. Despite fierce defense, the fortress fell, leading to a century of direct Mongol administration over Jeju (the Tamna Mangbu period) during which Mongolian horses and equestrian customs were introduced to the island.

Key Sights and Seasonal Flower Gardens:
1. Memorial Monument and Exhibition Hall:
   - Houses excavated iron arrowheads, armor fragments, pottery tiles inscribed with Goryeo military seals, and a sacred altar honoring the fallen warriors.
2. Earthen Rampart Walking Path (Totseong-gil):
   - A peaceful 2.5-km walking trail winding along the crest of the preserved grassy earthen walls, offering sweeping views of northern coastal waters and Aewol oreums.
3. Famous Flower Hotspots:
   - The fortress grounds are celebrated for seasonal floral fields: yellow rapeseed flowers in April, purple salvias in summer, and endless fields of pink cosmos and silver grass in autumn.

Visitor Details and Access:
- Admission: Free public entry.
- Operating Hours: Exhibition Hall open 09:00 to 18:00 daily. Earthen ramparts open 24/7.
- Public Transit: Blue Trunk Bus 291 or City Bus 455 to "Hangpaduri Entrance" stop.
"""

# ==============================================================================
# CATEGORY 7: FORESTS, HEALING TRAILS & GOTJAWAL (44 - 49)
# ==============================================================================

DOCUMENTS["44_bijarim_forest_ancient_nutmeg_sanctuary.txt"] = """Title: Bijarim Forest Ancient Nutmeg Tree Sanctuary Guide
Source: Cultural Heritage Administration & Gujwa-eup Forestry Office
Access Date: 2026-10-20
Category: Natural Monument & Primeval Forest

Overview:
Located in Pyeongdae-ri, Gujwa-eup, northeastern Jeju, Bijarim Forest (Natural Monument No. 374) is home to the largest single-species natural nutmeg tree (Torreya nucifera, or "Bija-namu") forest in the world. Spanning an area of over 448,000 square meters, this primeval woodland contains more than 2,800 ancient nutmeg trees ranging in age from 500 to 800 years.

Ecological and Therapeutic Features:
- Natural Phytoncide Sanctuary: Nutmeg trees release extraordinarily high concentrations of natural phytoncides (terpenes), known to reduce human stress hormones, lower blood pressure, and boost immune cell activity. The forest air carries a distinctive, soothing pine-nut aroma.
- Red Volcanic Scoria Paths (Songi-gil): The entire 2.2-kilometer forest trail is paved with natural red volcanic scoria ("Songi"), a porous volcanic mineral gravel rich in far-infrared minerals. Many visitors walk barefoot along the cool red paths.
- The Ancient Ancestor Tree (Millennium Bija Tree): Standing at the center of the forest is the revered "New Millennium Nutmeg Tree", which germinated roughly 820 years ago during the Goryeo Dynasty. Rising 14 meters high with a trunk circumference of nearly 6 meters, it is the oldest tree on Jeju Island.
- The "Lover Trees" (Yeonriji): Two distinct ancient nutmeg trees whose separate trunks grew together and fused into a single tree, symbolizing enduring love and fidelity.

Visitor Information, Admission, and Regulations:
- Walking Courses:
  - Short Course: 1.0 km loop (approx. 40 minutes, flat and stroller-accessible).
  - Long Course: 2.2 km full loop (approx. 1 hour 20 minutes, including stone paths).
- Operating Hours: Daily 09:00 to 18:00 (last entry at 17:00). Open year-round.
- Admission Fees: Adults (ages 25-64): 3,000 KRW; Youth/Military: 1,500 KRW; Children (7-12): 1,500 KRW; Seniors (65+): Free.
- Eco-Protection: Food, pets, bicycles, smoking, and collecting fallen nutmeg seeds or wild orchids are strictly prohibited.

Transportation:
- Take Blue Trunk Bus 211, 212, or Tourist Shuttle 810-1 directly to "Bijarim Forest" stop.
"""

DOCUMENTS["45_saryeoni_forest_trail_healing_red_cedars.txt"] = """Title: Saryeoni Forest Trail Healing Red Cedar Road Guide
Source: Jeju Special Self-Governing Province Forestry Institute
Access Date: 2026-10-20
Category: Healing Forest & Eco-Trekking

Overview:
The Saryeoni Forest Trail is a 15-kilometer protected forestry gravel road situated at an elevation of 500 to 600 meters in the mid-mountain forest zone of southeastern Jeju. Winding between the Bijarim-ro highway entrance in Jocheon-eup and the Namwon-eup Red Cedar Forest entrance, it is revered as the "Sacred Forest" (the name "Saryeoni" translates from native dialect to "spool of sacred yarn" or "sacred ground").

Trail Highlights and Forestry Ecosystem:
1. Towering Japanese Cedar Groves (Samnamu):
   - The southern section (near the Red Cedar Forest trailhead) features dense, soaring stands of Cryptomeria japonica planted in the 1930s. The trees reach heights of 25 to 30 meters, blocking direct sunlight and creating a serene, cathedral-like atmosphere.
2. Rich Biodiversity:
   - Home to wild roe deer (Noru), Jeju badgers, woodpeckers, and rare epiphytic wild orchids. The canopy blends Japanese cedars, sawtooth oaks (Chamnamu), and hornbeams.
3. Pure Natural Gravel and Red Songi:
   - The trail remains unpaved, surfaced with fine volcanic red scoria and river gravel, maintaining natural rainwater absorption.

Trail Lengths, Checkpoints, and Etiquette:
- The Complete Trek: A full one-way traverse between Bijarim-ro and Namwon-eup spans 15 km, taking approximately 3.5 to 4.5 hours of moderate walking.
- The Leisurely Section: Most casual travelers enter via the southern entrance on Road 1118 (Namwon / Hannam gate) and explore the flat 1.5-km wooden deck loop (approx. 45 minutes) through the densest cedar grove.
- Operating Hours: Daily 09:00 to 17:00 (hikers must enter before 16:00). In cases of heavy rainfall, typhoons, or high forest fire alerts, the trail is closed immediately for safety.
- Admission: 100% Free public admission year-round.
- Prohibitions: No vehicles, motorcycles, or bicycles allowed. No trash bins on the trail; visitors must pack out all waste.

Transportation:
- South Entrance (Cedar Forest): Take Red Express Bus 181 or Blue Bus 212/222 to "Saryeoni Forest Trail Entrance" stop.
- Limited parking along highway verges; public bus is strongly encouraged.
"""

DOCUMENTS["46_jeju_jeolmul_natural_recreation_forest.txt"] = """Title: Jeju Jeolmul Natural Recreation Forest Guide
Source: Jeju City Forestry Division & Jeolmul Management Office
Access Date: 2026-10-20
Category: Municipal Recreation Forest & Accessible Trails

Overview:
Located in Bonggae-dong, northeastern Jeju, Jeolmul Natural Recreation Forest encompasses over 300 hectares of cedar woodland at the foot of Jeolmul Oreum (elevation 697m). Its name originates from "Jeol" (Buddhist temple) and "Mul" (fresh water), referencing the pristine natural mineral spring located inside the forest grounds that has provided potable water for centuries.

Features and Accessibility:
1. 50-Year-Old Japanese Cedar Forest:
   - Planted densely since 1970, the tall, straight cedar trunks form a continuous green umbrella overhead, filtering cool, moist mountain air even during the hottest summer afternoons.
2. Premier Barrier-Free Boardwalks (Deck Trail):
   - Over 7 kilometers of flat, wide wooden boardwalk trails crisscross the forest floor with gentle inclines and zero steps, allowing elderly travelers, wheelchair users, and parents pushing baby strollers to explore deeply into the forest canopy safely.
3. Natural Jeolmul Mineral Spring:
   - A crystalline natural rock spring tested regularly for purity, safe for drinking directly from clean communal ladles.
4. Jeolmul Oreum Summit Trail:
   - A 1.6-kilometer wooden staircase trail ascends to the twin peak observation decks of Jeolmul Oreum (approx. 30 minutes up), offering sweeping views of Mount Hallasan's eastern crater walls and dozens of surrounding parasitic cones.

Visitor Facilities and Admission Fees:
- Operating Hours: 09:00 to 18:00 (March to October), 09:00 to 17:00 (November to February).
- Admission Fees: Adults (ages 19-64): 1,000 KRW; Youth/Military: 600 KRW; Children (7-12): 300 KRW; Seniors (65+): Free.
- Forest Lodge Accommodations: Traditional wooden forest cabins (Huyangnim Log Cabins) can be booked through the national "SoopNaDeulE" reservation portal.
- Parking: Large paid parking lot (3,000 KRW for standard vehicles).

Transportation:
- Take Blue Trunk Bus 212 or 222 from Jeju City Terminal directly to "Jeolmul Recreation Forest" terminus.
"""

DOCUMENTS["47_gotjawal_forest_the_lungs_of_jeju.txt"] = """Title: Gotjawal Forest Ecosystem (The Lungs of Jeju)
Source: Jeju Gotjawal Provincial Park & Gotjawal Conservation Foundation
Access Date: 2026-10-20
Category: Ecological Sanctuary & Geological Biosphere

Overview:
"Gotjawal" is a unique native Jeju term combining "Got" (dense forest) and "Jawal" (tangled brush and rocky boulders). It refers to an extraordinary primeval forest ecosystem formed exclusively on vast, uneven blocky aa-lava flows that erupted thousands of years ago. Because the jagged volcanic rock terrain was impossible to cultivate for agriculture, Gotjawal remained untouched by human development for centuries, functioning today as the vital "Lungs of Jeju" and the primary aquifer recharging underground freshwater.

Unique Microclimate and Biodiversity:
1. Coexistence of Tropical and Polar Flora:
   - The porous, fractured basalt lava rocks feature deep crevices and breathing holes called "Sumbigol", where subterranean air maintains a constant year-round temperature of 15°C with high humidity.
   - Consequently, tropical southern evergreen ferns flourish directly alongside northern sub-polar mosses and deciduous trees in the same forest grove—a biological phenomenon found nowhere else on Earth.
2. Freshwater Reservoir:
   - Rainwater does not form surface rivers in Gotjawal; instead, it filters instantaneously through the porous volcanic rubble, purifying as it descends into deep underground aquifers, creating Jeju's famous bottled mineral waters.
3. Jeju Gotjawal Provincial Park (Daejeong-eup):
   - A 1.5-million-square-meter protected eco-park featuring 5 thematic walking trails (totaling 6.7 km), an eco-observatory tower, and an interactive ecological exhibition center.

Visiting Guidelines (Gotjawal Provincial Park):
- Operating Hours: Daily 09:00 to 17:00 (last entry at 15:30 in winter, 16:00 in summer).
- Admission: Adults: 1,000 KRW; Youth: 800 KRW; Children: 500 KRW.
- Footwear Rule: The trail is rocky and uneven; flip-flops and high heels are strictly forbidden for safety reasons. Sneakers or hiking shoes are required.

Transit:
- Take Blue Trunk Bus 255 from Jeju Terminal to "Jeju Gotjawal Provincial Park" stop (approx. 45 minutes).
"""

DOCUMENTS["48_camellia_hill_and_botanical_gardens.txt"] = """Title: Camellia Hill and Subtropical Botanical Gardens Guide
Source: Camellia Hill Arboretum & Andeok-myeon Office
Access Date: 2026-10-20
Category: Botanical Garden & Floral Tourism

Overview:
Situated in Sangchang-ri, Andeok-myeon, southwestern Jeju, Camellia Hill is the largest camellia-themed botanical arboretum in East Asia, spanning over 200,000 square meters. The garden is home to more than 6,000 camellia trees representing 500 distinct species from over 80 countries, blooming in rotation throughout the autumn, winter, and early spring.

Seasonal Highlights:
1. Winter Camellia Splendor (November to February):
   - The peak season when vibrant pink, crimson, and snowy-white camellia petals blanket winding forest paths.
   - The "Camellia Petal Carpet Trail": Fallen blossom petals form a continuous red carpet beneath arching tree branches, recognized as one of the most romantic walking paths in Korea.
2. Summer Hydrangea Festival (June to August):
   - When camellia blossoms fade, vast outdoor gardens and greenhouse pavilions burst into millions of colorful blue, purple, and pastel hydrangeas (Sook-guk).
3. Autumn Silver Grass and Pink Muhly (September to October):
   - Features dedicated gardens of delicate pink muhly grass and golden pampas grass.
4. Traditional Thatched Pavilions and Reflecting Ponds:
   - Scenic tea cafes serving organic camellia flower tea, cold citrus beverages, and natural camellia seed cosmetic oils.

Visitor Hours, Admission, and Operations:
- Operating Hours: Open 365 days a year from 08:30 to 18:30 (summer), 08:30 to 18:00 (spring/autumn), 08:30 to 17:30 (winter). Last ticketing 1 hour before closure.
- Admission Fees: Adults (ages 19-64): 10,000 KRW; Teenagers: 8,000 KRW; Children (ages 3-12) & Seniors (65+): 7,000 KRW.
- Walking Time: Touring the full paved garden loop takes approx. 1.5 to 2 hours.

Transportation:
- Take Blue Trunk Bus 282 or 252 from Jeju Intercity Bus Terminal to "Donggwang Transfer Center", then transfer to Village Bus 752-1 to "Camellia Hill".
"""

DOCUMENTS["49_hallasan_ecoseungma_and_horse_pastures.txt"] = """Title: Jeju Horse Pastures (Jongma-mokjang) and Equine Heritage
Source: Jeju Special Self-Governing Province Livestock Research Institute
Access Date: 2026-10-20
Category: Equine Heritage & Traditional Ranching

Overview:
Jeju Island has been celebrated for over a millennium as the premier horse breeding capital of Korea, enshrined in the ancient proverb: "Send humans to Seoul and horses to Jeju." Today, the Jeju Horse (Jorangmal, Natural Monument No. 347) is preserved on the lush mid-mountain volcanic grasslands along the 516 Highway at the Jeju Horse Pasture (Jongma-mokjang), managed directly by the provincial government.

Equestrian History and Biology of Jorangmal:
- The Native Jeju Pony:
  - Measuring only 120 to 130 cm at the shoulder, the Jeju horse is compact and stocky, with extraordinarily dense bone structure, high endurance, and gentle temperament.
  - Adapted over centuries to rocky volcanic slopes, it can navigate steep basalt terrain where larger mainland warhorses would stumble.
  - History: Mongolian horses introduced during the Yuan Dynasty in the 13th century cross-bred with indigenous Tamna ponies, establishing specialized royal breeding herds.
- The 516 Highway Horse Pastures (Jongma-mokjang):
  - A vast 90-hectare government pasture located along Highway 516 in Yonggang-dong.
  - From April to October, over 100 purebred Jeju ponies roam freely across rolling emerald hills, feeding on wild clover and volcanic grasses with Mount Hallasan rising behind them.

Visitor Information:
- Admission: Free public roadside viewing platforms and raised wooden observation boardwalks.
- Operating Hours: Open 24/7; horses are grazing outdoors from mid-April through late October (retracted to indoor winter barns during freezing snow months).
- Horseback Riding Stables (Seungma): Commercial tourist riding grounds along the mid-mountain roads offer 15-to-30-minute introductory horseback rides for beginners (approx. 15,000 - 30,000 KRW).

Transportation:
- Take Blue Trunk Bus 281 along Highway 516 to "Jeju Horse Pasture (Jongma-mokjang)" stop (approx. 20 minutes from Jeju City).
"""

# ==============================================================================
# CATEGORY 8: MUSEUMS & ART CENTERS (50 - 53)
# ==============================================================================

DOCUMENTS["50_jeju_national_museum.txt"] = """Title: Jeju National Museum Maritime and Archaeology Guide
Source: National Museum of Korea & Jeju National Museum
Access Date: 2026-10-20
Category: National Museum & Ancient History

Overview:
Located in Sara-dong, eastern Jeju City, near Sarabong Peak, the Jeju National Museum is a premier national cultural institution dedicated to collecting, preserving, and exhibiting the unique archaeological, historical, and maritime heritage of Jeju Island and the ancient Tamna Kingdom.

Exhibition Galleries and Key Artifacts:
1. Prehistoric and Early Tamna Gallery:
   - Displays polished stone tools, dolmen relics, and red-burnished pottery excavated from the Samyang-dong prehistoric settlement (1st century BC), the largest Bronze Age village site in southern Korea.
2. The Tamna Kingdom Epoch:
   - Showcases artifacts testifying to ancient Tamna's extensive maritime trade networks with Baekje, Silla, Tang Dynasty China, and ancient Yamato Japan, including bronze mirrors, foreign coins, and jade comma-beads.
3. Goryeo and Joseon Dynasty Heritage:
   - Features Buddhist temple bells, stone pagodas, royal administrative seals, and artifacts from the Sambyeolcho anti-Mongol rebellion at Hangpaduri.
4. Immersion Media Art Hall:
   - A modern 360-degree digital projection hall showcasing "The Ocean of Tamna", an animated historical presentation of ancient mariners navigating stormy seas to Mount Hallasan.
5. Children's Discovery Museum:
   - Interactive hands-on archeological digging, rubbing stations, and traditional Korean architectural puzzle models.

Hours, Admission, and Amenities:
- Admission: 100% Free permanent admission for all visitors.
- Operating Hours: Tuesday to Sunday 09:00 to 18:00 (last admission 17:30). Closed every Monday, January 1, Lunar New Year's Day, and Chuseok.
- Free audio guides available in English, Korean, Japanese, and Chinese.

Transportation:
- Located a 15-minute drive from Jeju International Airport. Take City Bus 312, 325, 326, or 380 to "Jeju National Museum" stop.
"""

DOCUMENTS["51_jeju_stone_park_and_seolmundae_myth.txt"] = """Title: Jeju Stone Park and Seolmundae Halmang Folklore Guide
Source: Jeju Stone Park Management Office & Cultural Heritage Bureau
Access Date: 2026-10-20
Category: Sculpture Park & Island Folklore

Overview:
Encompassing over 3 million square meters of pristine volcanic woodland in Gyorae-ri, Jocheon-eup, Jeju Stone Park is an extraordinary open-air museum and ecological sculpture sanctuary. Built over 20 years to honor the geological, cultural, and spiritual essence of Jeju's volcanic stones, it is centered around the mythological creation legend of Grandma Seolmundae (Seolmundae Halmang), the giant creator goddess of Jeju.

Key Highlights and Architectural Masterpieces:
1. The Sky Pond (Haneul Yeonmot):
   - A monumental circular stone infinity pond measuring 40 meters in diameter, built atop the underground museum roof. The calm water mirrors the sky and surrounding oreums, creating a meditative visual gateway to the park.
2. The Myth of the 500 Generals (Obaek-Janggun):
   - Legend tells that Grandma Seolmundae was an immense giant who created Mount Hallasan by scooping earth into her skirt. She had 500 giant sons. During a severe famine, while brewing a huge cauldron of soup for her sons, she accidentally slipped and fell into the boiling pot. Returning home famished, the sons ate the soup before the youngest son discovered their mother's bones at the bottom. Overcome with grief, the youngest fled south to Chagwido, while the remaining 499 brothers wept endlessly on the mountain until they turned to stone—forming the craggy rock spires of Yeongsil Giam on Hallasan.
3. The Field of 500 Stone Generals:
   - Hundreds of dramatic natural volcanic rock monoliths standing like ancient sentinels along the forest paths.
4. Underground Stone Museum:
   - Carved deeply beneath the volcanic earth, displaying rare mineral crystals, lava stalactites, volcanic bombs, and traditional stone tools (grindstones, stone mortars, and tomb guardian statues).

Visiting Information:
- Operating Hours: Daily 09:00 to 18:00 (last entry 17:00). Closed on the first Monday of every month.
- Admission Fees: Adults (ages 19-64): 5,000 KRW; Youth/Military: 3,500 KRW; Seniors (65+) and children under 12: Free.
- Eco-Electric Train: An open-air electric train tours the expansive 3-kilometer outer route (5,000 KRW).

Transportation:
- Take Blue Trunk Bus 212 or 222 from Jeju City Terminal directly to "Jeju Stone Park" stop.
"""

DOCUMENTS["52_osulloc_tea_museum_and_seogwang_plantations.txt"] = """Title: Osulloc Tea Museum and Seogwang Green Tea Plantation
Source: Amorepacific Heritage Foundation & Andeok-myeon Office
Access Date: 2026-10-20
Category: Tea Culture & Agricultural Tourism

Overview:
Situated in Seogwang-ri, Andeok-myeon, the Osulloc Tea Museum opened in 2001 as South Korea's first tea culture museum, attracting over 1.5 million visitors annually. Established by Amorepacific founder Suh Sung-whan, who transformed rocky, uncultivated volcanic wasteland into thriving organic tea plantations in the late 1970s, it is surrounded by the vast Seogwang Tea Garden—one of the largest organic tea estates in the country.

Key Facilities and Tea Experiences:
1. The Tea Culture Museum:
   - Shaped like a traditional tea cup, the museum displays historical ceramic teaware from the Three Kingdoms, Goryeo, and Joseon periods, showcasing the philosophical evolution of Korean tea ceremonies (Dado).
   - Live Tea Master Roasting: Master tea roasters demonstrate manual pan-firing and rolling of fresh green tea leaves on hot cast-iron kettles.
2. Observatory Tower:
   - A three-story glass observation deck overlooking the rolling green carpets of the Seogwang tea fields, Sanbangsan mountain, and distant southern coasts.
3. Innisfree Jeju House:
   - An adjacent eco-beauty complex featuring natural cosmetics made from Jeju organic green tea, volcanic cluster clay, camellia oil, and Hallabong citrus. Offers organic soap-making workshops and a cafe serving black pork sausage brunch platters.
4. Signature Cafe Menu:
   - World-famous for rich green tea soft-serve ice cream, matcha Swiss roll cakes, and iced Jeju Hallabong green tea coolers.

Visitor Information:
- Admission: Free general admission to the museum, tea fields, and Innisfree House.
- Operating Hours: Open daily from 09:00 to 18:00 (summer until 19:00). Open 365 days.
- Tea Stone Premium Classes: 45-minute structured tea tasting and ceremony classes in the standalone glass pavilion (approx. 30,000 KRW, online advance reservation required).

Transportation:
- Take Blue Trunk Bus 255 from Jeju Intercity Terminal directly to "Osulloc" stop (approx. 50 minutes).
"""

DOCUMENTS["53_arte_museum_jeju_immersive_digital_media.txt"] = """Title: Arte Museum Jeju Immersive Digital Media Art
Source: d'strict Holdings & Aewol-eup Municipal Council
Access Date: 2026-10-20
Category: Digital Media Art & Indoor Attractions

Overview:
Located in Eoeum-ri, Aewol-eup, in western Jeju, Arte Museum Jeju is South Korea's premier large-scale immersive digital media art exhibition. Spanning a floor area of 4,600 square meters with towering 10-meter ceilings in a converted former optical loudspeaker manufacturing plant, the museum was created by the world-renowned digital design company d'strict (creators of the iconic "WAVE" anamorphic illusion at COEX Seoul).

Exhibition Concept ("Eternal Nature"):
The exhibition comprises 10 distinct multimedia zones recreating the breathtaking forces and textures of nature through cutting-edge projection mapping, sensory soundscapes, and customized aromatic scent design:
1. "WATERFALL INFINITE": A 14-meter-high virtual waterfall roaring down mirrored walls, creating an infinite visual chasm of falling water.
2. "BEACH AURORA": A glowing nighttime ocean shore where rhythmic waves wash over sand beneath shifting northern aurora skies.
3. "FLOWER CAMELLIA": Endless mirrored fields of fluttering camellia petals and blooming blossoms responding dynamically to visitors' movements.
4. "GARDEN": An enormous central hall displaying the masterworks of Western Art History (Gustav Klimt, Van Gogh, Claude Monet) morphing gracefully across 10-meter screens, followed by a tribute to the light and natural splendor of Jeju Island.
5. "ARTE TEA BAR": An interactive tea salon where a virtual camellia blossom blooms in real time inside your cold green tea cup using computer vision tracking.

Visitor Hours, Ticketing, and Guidelines:
- Operating Hours: Daily 10:00 to 20:00 (last entry at 19:00). Open year-round.
- Admission Fees: Adults (ages 19+): 17,000 KRW; Youth (14-18): 13,000 KRW; Children (8-13): 10,000 KRW; Infants (3-7): 8,000 KRW.
- Indoor Attraction: Highly recommended during rainy days, typhoons, or hot summer afternoons.
- Photography: Flash photography, tripods, and food/beverages are strictly prohibited inside the galleries.

Transportation:
- Take Blue Bus 251, 252, 253, 254 to "Donggwang Transfer Center", then take local taxi (approx. 7 minutes / 6,000 KRW) or Bus 784-1 to "Arte Museum".
"""

# ==============================================================================
# CATEGORY 9: JEJU OLLE DETAILED COURSES (54 - 56)
# ==============================================================================

DOCUMENTS["54_jeju_olle_network_and_passport_system.txt"] = """Title: Jeju Olle Trail Network and Official Passport System
Source: Jeju Olle Foundation & Jeju Special Self-Governing Province
Access Date: 2026-10-20
Category: Walking Trails & Ecotourism Network

Overview:
The Jeju Olle Trail is a world-famous network of long-distance walking paths circumnavigating the entire coastline, sub-islands, and foothills of Jeju Island. Founded in 2007 by former journalist Suh Myung-sook, the word "Olle" originates from the traditional Jeju dialect, referring to the narrow, curved stone alley connecting a house's front door to the main village street. Today, the network comprises 27 official courses (21 main numbered coastal routes and 6 sub-island routes) totaling 437 kilometers.

Official Signposts and Visual Wayfinding Markers:
1. The Ganse (Jeju Pony):
   - Blue wooden signposts shaped like native Jeju ponies pointing the direction of travel. The head points forward; a QR code on the saddle provides map coordinates.
2. Dual-Colored Ribbons:
   - Pairs of blue (representing Jeju's clear sea) and orange (representing Jeju's ripe mandarin oranges) ribbons tied to tree branches, fences, and utility poles every 50 to 100 meters.
3. Arrow Markers:
   - Blue arrows painted on walls and basalt rocks indicate the regular forward route; orange arrows indicate the reverse trekking route.

The Official Olle Passport and Completion Certification:
- Olle Passport (18,000 KRW):
  - Hikers collect unique stamp seals at three checkpoints on every route: Start, Midpoint, and Terminus.
- Official Completion Medals & Certificates:
  - "Full Trail Completion": Walking all 27 courses (437 km) awards an official framed certificate, personal medal, and your name inscribed on the Hall of Fame at the Jeju Olle Traveler Center in Seogwipo.
  - Over 20,000 domestic and international walkers have completed the full trail.

Safety Rules and Eco-Trekking Etiquette:
- Clean Olle Campaign: Hikers receive biodegradable trash bags to collect roadside litter ("Plogging").
- Quiet Trekking: Respect privacy when passing through residential farm villages; do not pick agricultural citrus from orchards.
- Emergency Contact: Jeju Olle Call Center (+82-64-762-2190) and Police Emergency (112).
"""

DOCUMENTS["55_jeju_olle_trail_route_07_oedolgae_to_wolpyeong.txt"] = """Title: Jeju Olle Trail Route 7 (Oedolgae to Wolpyeong) Guide
Source: Jeju Olle Foundation & Seogwipo City Tourism Bureau
Access Date: 2026-10-20
Category: Walking Trails & Coastal Scenery

Overview:
Olle Route 7 is celebrated among hikers as the most scenic and beloved coastal route in the entire 437-km Jeju Olle network. Extending 17.6 kilometers from the Jeju Olle Traveler Center in downtown Seogwipo to the quiet seaside hamlet of Wolpyeong village, it winds along dramatic vertical sea cliffs, peaceful pine forests, and rocky coastal coves.

Key Route Checkpoints and Landmarks:
1. Start Point: Jeju Olle Traveler Center (Downtown Seogwipo):
   - The global headquarters of the trail, featuring an information cafe, official passport sales, and eco-lodging.
2. Oedolgae Rock (Lonely Rock):
   - A dramatic 20-meter natural sea stack rising out of ocean surf, formed roughly 1.5 million years ago. Legend tells that during the Goryeo Dynasty, General Choe Yeong disguised the rock as a giant military general to frighten invading Mongolian forces into retreat.
3. Dombe-nang Coastal Cliff Path:
   - A wooden boardwalk perched above sheer basalt cliffs, shaded by Japanese black pines with panoramic vistas of Beomseom (Tiger Island).
4. Subong-ro and Beopwhan Port:
   - "Subong-ro" was hand-carved out of rocky seaside cliffs using pickaxes by dedicated trail volunteer Kim Su-bong in 2007.
   - Beopwhan Port is the southernmost harbor in South Korea and an active traditional Haenyeo diving center.
5. Gangjeong Stream and Wolpyeong Terminus:
   - Where pristine mountain freshwater streams rush across smooth volcanic bedrock directly into the sea.

Trail Statistics and Tips:
- Total Distance: 17.6 km.
- Walking Time: Approx. 5 to 6 hours at a steady pace.
- Difficulty: Intermediate (mostly flat wooden boardwalks and paved coastal paths, with some rocky boulder beaches requiring sturdy hiking shoes).
- Midpoint Stamp: Located at Beopwhan Haenyeo Experience Center (7.8 km mark).

Transit:
- Start point: Walkable from downtown Seogwipo hotels or take Bus 600 from airport to "Seogwipo Kal Hotel".
- Finish point: Take Blue Bus 202 or 521 from Wolpyeong Village back to downtown Seogwipo.
"""

DOCUMENTS["56_jeju_olle_trail_route_10_hwasun_to_moseulpo.txt"] = """Title: Jeju Olle Trail Route 10 (Hwasun to Moseulpo) Guide
Source: Jeju Olle Foundation & Daejeong-eup Municipal Council
Access Date: 2026-10-20
Category: Walking Trails & Modern History

Overview:
Extending 15.6 kilometers from Hwasun Golden Sand Beach to Hamo Port in Moseulpo, Olle Route 10 combines geological grandeur with somber reflections on modern Korean history. The route hugs southwestern coastlines, offering unobstructed perspectives of Mount Sanbangsan, Songaksan Mountain, and the historic Japanese military installations of World War II.

Key Highlights and Checkpoints:
1. Hwasun Golden Sand Beach and Marine Geotrail:
   - Begins on black-and-gold sands featuring natural cold freshwater springs flowing from volcanic rock crevices.
2. Yongmeori Coast and Sanbangsan Foothills:
   - Passes the foot of Sanbangsan before traversing the scenic coastal sand dunes of Sagye Beach.
3. Songaksan Mountain Coastal Path:
   - A double-crater volcano protruding into the sea. The clifftop boardwalk offers world-class views of Gapado and Marado islands on the horizon.
   - Japanese Coastal Artillery Caves: The seaside cliffs beneath Songaksan are honeycombed with 15 man-made caves excavated by the Imperial Japanese Army in 1945 using forced Korean labor to conceal suicide torpedo boats.
4. Altteureu Airfield and Anti-Aircraft Bunkers:
   - Traversing the flat coastal plains of Daejeong reveals the remnants of a massive 1930s Japanese military airfield used during the Second Sino-Japanese War, including 19 preserved concrete aircraft hangars, an underground command bunker, and modern peace art sculptures.

Trail Statistics:
- Total Distance: 15.6 km (approx. 4 to 5 hours).
- Difficulty: Easy to moderate (very gentle terrain, gentle wooden stairs around Songaksan).
- Midpoint Stamp: Located at the Songaksan Tourist Parking Information Booth.
- Finish: Hamo Port (ferry hub for Marado and Gapado).

Transit:
- Start: Take Blue Bus 202 or 252 to "Hwasun-ri" stop.
- Finish: Take Express Bus 151 or 152 from Moseulpo Transfer Center back to Jeju City.
"""

# ==============================================================================
# CATEGORY 10: CULINARY TRADITIONS & MARKETS (57 - 60)
# ==============================================================================

DOCUMENTS["57_jeju_black_pork_and_traditional_meljot.txt"] = """Title: Jeju Black Pork and Traditional Meljot Culinary Guide
Source: Jeju Tourism Organization & Jeju Livestock Cooperative
Access Date: 2026-10-20
Category: Gastronomy & Food Culture

Overview:
Jeju Black Pig (Heukdwaeji, Natural Monument No. 550) is the most celebrated culinary delicacy of Jeju Island. Endemic to the island's volcanic terrain for over a millennium, these small, hardy pigs are characterized by coarse black hair, small narrow snouts, and lean, densely marbled meat that yields a distinctive nutty, chewy, and deeply savory flavor unlike standard commercial pork.

Culinary Preparation and The Meljot Tradition:
1. Thick Charcoal Grilling (Geun-gogi):
   - In traditional Jeju restaurants, black pork is served as "Geun-gogi" (sold by the "Geun", an ancient unit equal to 600 grams) in monumental slabs measuring 4 to 5 cm in thickness.
   - Slices of pork belly (Samgyeopsal) and pork neck (Moksal) are grilled slowly over natural charcoal or volcanic briquettes, crisping the outer rind while locking in rich internal juices.
2. The Boiling Anchovy Dip (Meljot):
   - Authentic Jeju black pork is never dipped in plain salt or sweet sauce; it is paired with "Meljot"—a pungent, salted dipping sauce made from fermented large anchovies caught off Seogwipo.
   - The metal sauce cup (containing chopped garlic, red chili, soju, and fermented anchovies) is placed directly on the burning charcoal briquettes beneath the grill until it boils vigorously, mellowing its pungency and transforming it into an umami-rich dip that cuts through the pork's rich fat.

Traditional Breeding Lore (Dottongsi):
- Historically, black pigs were raised inside "Dottongsi"—traditional outdoor stone pigsties positioned beneath family outhouses. The pigs consumed kitchen scraps, agricultural waste, and human waste, acting as efficient sanitary recyclers while producing rich organic fertilizer for volcanic fields. This practice was completely phased out in the 1960s; modern black pigs are raised under strict hygienic municipal standards.

Famous Dining Streets:
- Black Pork Street (Heukdwaeji Geori) in downtown Jeju City (near Dongmun Market).
- Jungmun Black Pork Street in Seogwipo.
"""

DOCUMENTS["58_gogi_guksu_and_traditional_soups.txt"] = """Title: Jeju Gogi Guksu and Traditional Folk Soups
Source: Jeju Food Culture Research Institute & VisitJeju
Access Date: 2026-10-20
Category: Local Cuisine & Traditional Soups

Overview:
Unlike mainland Korean noodle dishes that rely on anchovy, beef bone, or chicken broth, traditional Jeju noodles are defined by "Gogi Guksu" (Pork Noodle Soup), a hearty, comforting bowl reflecting the island's historical agricultural customs and celebratory wedding feasts.

Key Traditional Dishes:
1. Gogi Guksu (Pork Noodle Soup):
   - Broth: Thick pork bones are simmered for 12 to 18 hours until the broth turns rich, milky white, and naturally creamy.
   - Noodles: Yellowish, thick wheat flour noodles (Jung-myeon), cooked to an al dente chewiness.
   - Topping: Generously topped with thick, tender slices of boiled Jeju pork belly, chopped scallions, sesame seeds, and crushed dried seaweed (gim).
   - Seasoning: Seasoned with salt, black pepper, and spicy red pepper powder (Gochugaru) to taste.
2. Dombe Gogi (Cutting-Board Boiled Pork):
   - High-grade Jeju pork belly boiled gently with soybean paste, ginger, garlic, and soju until meltingly tender.
   - In the native dialect, "Dombe" means a heavy wooden cutting board. The boiled meat is sliced directly in front of the diner and served immediately on the rustic wooden board with sea salt, fermented baby shrimp (Saeujeot), and pickled garlic scapes.
3. Momguk (Gulfweed and Pork Bone Soup):
   - A traditional ceremonial soup cooked during village weddings and funerals.
   - Made by boiling pork broth with "Mom" (Sargassum / gulfweed sea algae), tender pork meat, and buckwheat flour (Memil), resulting in a thick, deeply earthy, and nutrient-rich maritime chowder.

Famous Dining Locations:
- Noodle Street (Guksu Geori) in Samseong-dong, Jeju City (fronting Samseonghyeol and the Natural History Museum), where dozens of specialty noodle houses operate 24 hours daily. Average price: 9,000 to 10,000 KRW per bowl.
"""

DOCUMENTS["59_dongmun_traditional_market_and_night_market.txt"] = """Title: Dongmun Traditional Market and Night Market Guide
Source: Dongmun Traditional Market Merchants Association & Jeju City
Access Date: 2026-10-20
Category: Traditional Markets & Night Street Food

Overview:
Established in 1945 in Ildo-dong, downtown Jeju City, Dongmun Traditional Market is the oldest, largest, and busiest permanent commercial market on Jeju Island. Spanning 12 interconnected alleys and housing over 1,000 stalls, it serves as both the essential daily grocery hub for local residents and the premier culinary market for domestic and international travelers.

Market Zones and Specialty Sections:
1. Fresh Seafood Alley:
   - Freshly caught Silver Hairtail (Galchi), Red Seabream, Tilefish (Okdom), and live abalone.
   - Prepared Sashimi Stalls: Merchants package fresh assorted sashimi plates (raw flounder, sea bream, and mackerel) chilled on ice for only 10,000 to 15,000 KRW per platter for easy takeout.
2. Jeju Citrus and Fruit Section:
   - Hundreds of vibrant fruit stalls displaying seasonal native citrus varieties: Hallabong (sweet and bumpy-topped), Cheonhyehyang (fragrant thin-skinned), Redhyang (deep orange and firm), and sweet winter mandarins (Gyul).
   - Stalls provide nationwide and international insured boxed shipping.
3. Traditional Rice Cakes and Snacks:
   - Freshly made Omegit-tteok (millet bean cakes), sweet citrus tarts, Hallabong chocolates, and peanut rice snacks.
4. The Dongmun Night Market (Gate 8):
   - Opens every evening at 18:00 (operating until 24:00), transforming Gate 8 into an energetic culinary street food festival.
   - Over 30 specialized food stalls staffed by young chefs using culinary blowtorches: grilled black pork belly skewers, abalone gimbap rolls, spicy butter lobster tails, Hallabong ice cream, and rolled pork quesadillas accompanied by lively K-pop music.

Practical Traveler Tips:
- Operating Hours: General market open 08:00 to 21:00; Night Market open 18:00 to 24:00 daily.
- Payment: Credit cards, T-money transit cards, and mobile payments (KakaoPay, Alipay, WeChat Pay) are widely accepted across almost all stalls.
- Parking: A multi-story municipal parking garage is located at Gate 8 (first 30 minutes free).

Transportation:
- Located in downtown Jeju City, 15 minutes by bus from Jeju Airport. Take City Bus 316, 325, 365, or 465 to "Dongmun Market" stop.
"""

DOCUMENTS["60_seogwipo_maeil_olle_market.txt"] = """Title: Seogwipo Maeil Olle Market Culinary and Souvenir Guide
Source: Seogwipo Maeil Olle Market Merchants Association & VisitJeju
Access Date: 2026-10-20
Category: Traditional Markets & Street Food

Overview:
Located in the heart of Seogwipo City, Seogwipo Maeil Olle Market was founded in the early 1960s and has grown into the southern coast's premier cultural and culinary market. Covered by a soaring 620-meter arched weather-proof canopy with natural water canals running down the central walking corridor, it integrates directly into Jeju Olle Trail Route 6.

Key Culinary Highlights and Street Food:
1. Central Garden Rest Stream:
   - Running along the center of the main market lane is a landscaped stone waterway populated with swimming carp and surrounded by wooden benches where visitors can sit comfortably and enjoy street food purchases.
2. Signature Market Delicacies:
   - Modakchigi: An iconic Seogwipo comfort dish where tteokbokki (spicy rice cakes), gimbap, fried vegetable fritters, and boiled eggs are served together in a single large platter drenched in sweet and spicy chili sauce.
   - Garlic Fried Chicken (Maneul Tongdak): Whole crispy fried chicken tossed with freshly crushed local Daejeong garlic, served in steaming brown paper bags.
   - Heukdwaeji Croquettes and Skewers: Crispy fried potato croquettes stuffed with seasoned minced black pork and mozzarella cheese.
   - Hallabong Juice: Freshly squeezed 100% natural citrus juice served in whimsical Dolhareubang-shaped plastic bottles.
3. Souvenir Shops:
   - Hand-poured citrus scented candles, Jeju basalt lava stone diffusers, Dolhareubang plush toys, and local craft beers (Jeju Wit Ale).

Operating Hours, Facilities, and Location:
- Operating Hours: Daily 07:00 to 21:00 (summer until 21:30). Open all year round.
- Parking: Large 500-vehicle municipal parking tower with automated license plate recognition.
- Proximity: A 5-minute walk from Lee Jung-seob Art Street and a 15-minute walk down to Cheonjiyeon Waterfall.

Transportation:
- From Jeju International Airport, take Airport Limousine Bus 600 directly to "New Kyungnam Hotel" or "Seogwipo Downtown", then walk 5 minutes.
"""
print(f"Batch 3 compiled: {len(DOCUMENTS)} documents ready.")
