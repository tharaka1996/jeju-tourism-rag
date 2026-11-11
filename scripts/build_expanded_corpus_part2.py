"""
Corpus Expansion Script Part 2 for Jeju Tourism RAG Assistant.
Covers Oreums, Waterfalls, Valleys, and Sub-Islands (Documents 20 to 37).
"""

from pathlib import Path

DOCS_DIR = Path(__file__).resolve().parent.parent / "data" / "documents"
DOCS_DIR.mkdir(parents=True, exist_ok=True)

DOCUMENTS = {}

# ==============================================================================
# CATEGORY 3: OREUMS (VOLCANIC CONES) (20 - 26)
# ==============================================================================

DOCUMENTS["20_darangshi_oreum_queen_of_oreums.txt"] = """Title: Darangshi Oreum (Queen of Oreums) Visitor Guide
Source: Gujwa-eup Municipal Council & Jeju Oreum Conservation Committee
Access Date: 2026-10-20
Category: Volcanic Oreums & Mountain Trekking

Overview:
Rising to an altitude of 382.4 meters (with a relative height of 227 meters) in Songdang-ri, Gujwa-eup, Darangshi Oreum (also known as Wolrangbong, meaning "Moon-embracing Peak") is universally revered by Jeju mountaineers as the "Queen of Oreums." Its majestic, near-perfect conical symmetry and extraordinary funnel-shaped crater make it one of the most prominent geological landmarks on eastern Jeju.

Geological Features and Hiking Experience:
- The Giant Caldera Crater: The summit crater plunges to an astonishing depth of 115 meters—equal to the depth of Mount Hallasan's Baeknokdam crater lake. Walking along the 1.5-kilometer crater rim trail takes about 30 minutes and provides dramatic perspectives into the steep, grassy volcanic funnel.
- Summit Panorama: From the summit observation pavilion, hikers enjoy breathtaking 360-degree vistas stretching from Seongsan Ilchulbong and Udo Island on the eastern coast to the Hallasan mountain ridge in the west.
- Well-Maintained Staircase Trail: A 1.2-kilometer continuous wooden and rubber-mat staircase climbs the southeastern slope through Japanese cedar and pine groves. It takes approximately 40 to 50 minutes of steady uphill hiking to reach the crater rim.
- Neighboring Akkeundarangshi: Directly to the east sits "Akkeundarangshi Oreum" (Little Darangshi), an easily accessible mini-cone whose low crater rim fills with silver pampas grass in October.

Visitor Rules and Practical Information:
- Admission Fee: Free admission year-round.
- Facilities: Clean public restrooms, an automatic air-gun shoe dust cleaner, and a paved parking lot at the trailhead.
- Safety: Sturdy walking shoes or hiking boots are strongly recommended due to the steep continuous stair incline. Trekking poles with rubber tips are allowed.
- Open Hours: Open daily from sunrise to sunset.

Transportation:
- From Jeju City Intercity Bus Terminal, take Blue Bus 212 or 222 to "Songdang-ri Village", then take a local taxi (approx. 7 minutes / 6,000 KRW) or transfer to Village Bus 711-1 to "Darangshi Oreum Entrance".
"""

DOCUMENTS["21_yongnuni_oreum_gentle_ridgelines.txt"] = """Title: Yongnuni Oreum Gentle Ridgelines and Photography Guide
Source: Jeju Oreum Preservation Society & VisitJeju
Access Date: 2026-10-20
Category: Volcanic Oreums & Scenic Photography

Overview:
Yongnuni Oreum ("Dragon Eye Mountain") is a 247.8-meter-high volcanic cone located in Jongdal-ri, Gujwa-eup. Celebrated for its gentle, rolling contours and soft feminine ridgelines, it is perhaps the most beloved and accessible oreum on Jeju Island. The famous landscape photographer Kim Young-gap spent decades capturing its changing shadows, mist, and winds before his passing.

Geological Formations and Trails:
- Triple Crater Morphology: The summit consists of three interconnected, bowl-shaped craters formed by multiple gentle pyroclastic eruptions.
- Gentle Slopes: Unlike the steep staircases of Darangshi, Yongnuni features smooth grassy paths with a very gentle gradient, making it accessible to hikers of all fitness levels, including young children and seniors.
- Trail Length & Time: The round-trip loop trail is roughly 2.3 kilometers long, taking about 40 to 50 minutes at a leisurely walking pace.
- Free-Roaming Grazing Horses: Local farmers graze Jeju native horses and cattle on the open grassy slopes, adding pastoral charm as horses feed peacefully alongside the walking path.

Ecological Recovery and Rest Periods:
- Natural Resting System (Hyusikshikje): To combat severe vegetation erosion caused by millions of tourists, Jeju Special Self-Governing Province placed Yongnuni Oreum under an official 2-year mandatory ecological rest period from 2021 to 2023. It has since reopened with reinforced coconut-fiber mats and restricted off-trail walking boundaries.
- Strict Regulations: Leaving designated marked trails or stepping on recovering grassy slopes is strictly prohibited and carries fines under the Natural Parks Protection Act.

Visitor Details and Access:
- Admission: Free of charge.
- Parking: Free parking area with restrooms at the base.
- Public Transit: Blue Trunk Bus 212 or Tourist Shuttle Bus 810-1/810-2 stops at "Yongnuni Oreum" trailhead.
"""

DOCUMENTS["22_saebyul_oreum_and_fire_festival.txt"] = """Title: Saebyul Oreum and Jeju Fire Festival Guide
Source: Aewol-eup Office & Jeju City Culture and Tourism Bureau
Access Date: 2026-10-20
Category: Volcanic Oreums & Cultural Festivals

Overview:
Saebyul Oreum is a prominent volcanic peak located in Bongseong-ri, Aewol-eup, along the Pyeonghwa-ro highway in western Jeju. Rising to an altitude of 519.3 meters (relative height of 119 meters), its name translates to "Morning Star Peak", as it stands solitary and bright in the western evening sky. It is world-renowned as the primary ceremonial venue for the annual Jeju Fire Festival (Jeju Deulbul Festival).

Key Highlights and Seasonal Changes:
1. Autumn Silver Pampas Grass (Eoksae):
   - From late September through November, the entire mountain is transformed into a shimmering ocean of golden-white pampas grass dancing in the wind.
   - It is considered the premier autumn photography hotspot in western Jeju.
2. The Jeju Fire Festival (Jeju Deulbul Festival):
   - Held annually in early spring (March) based on the traditional agrarian custom of burning old winter pastures (Bang-ae) to eradicate harmful insects, pests, and old withered grasses while fertilizing the soil with ash.
   - The highlight of the festival is the dramatic full-scale torching of an entire side of the mountain (covering 300,000 square meters) accompanied by fireworks and traditional folk prayers for health and prosperous harvests.
3. Steep Summit Climb:
   - The west trail ascends directly up a steep 35-degree grassy slope. Although short (only 15 to 20 minutes to the top), it requires good footwear.
   - The summit ridge offers panoramic views of Hallasan, Biyangdo Island, Saebil Cafe (a converted former resort hotel), and nearby Idobong Oreum.

Visitor Guidelines:
- Admission: Free public access year-round.
- Facilities: Ample free parking accommodating hundreds of vehicles, clean restrooms, and local food trucks selling Hallabong juice and Jeju black pork hotdogs.
- Transportation: Take Blue Trunk Bus 251, 252, 253, 254, or 255 from Jeju Intercity Bus Terminal directly to "Hwajeon Village / Saebyul Oreum" bus stop (approx. 35 minutes).
"""

DOCUMENTS["23_abu_oreum_circular_crater_cedars.txt"] = """Title: Abu Oreum (Snug Oreum) and Pine Ring Guide
Source: Gujwa-eup Office & VisitJeju
Access Date: 2026-10-20
Category: Volcanic Oreums & Film Locations

Overview:
Abu Oreum (officially named "Ap-oreum", meaning "Father Oreum" or "The Oreum Sitting in Front") is located in Songdang-ri, Gujwa-eup. Rising only 51 meters above its surrounding base (elevation 301 meters), it is famous for its shallow, gentle outer slope contrasted with a remarkably wide, perfectly circular crater measuring over 500 meters in diameter and 78 meters deep.

Unique Landscape and Film Heritage:
- The Circular Japanese Cedar Ring: In the center of the vast bowl-shaped crater floor, a dense concentric ring of Japanese cedar and pine trees was artificially planted in the late 1960s. Seen from the crater rim, this circular evergreen tree formation creates a mysterious, otherworldly amphitheater appearance.
- Easy 5-Minute Ascent: Because the outer slope is exceptionally low, hikers reach the crater rim in just 5 to 7 minutes of easy walking along an unpaved grass path.
- The 1.4-km Rim Promenade: The entire crater rim trail is a flat, scenic loop that can be circumnavigated in 20 minutes, offering continuous views of grazing cows and surrounding volcanic cones.
- Cinematic Legacy: Served as the primary filming location for the acclaimed 1999 Korean film "The Uprising" (Lee Jae-su's Rebellion) and popular K-pop music videos.

Visitor Rules and Access:
- Admission: Free public entry 24/7.
- Amenities: Unpaved parking lot at the trailhead; no public restrooms (travelers should use facilities in nearby Songdang village).
- Livestock Etiquette: Abu Oreum is an active pasture. Visitors must securely close wooden farm gates behind them to prevent livestock from wandering onto the highway.
- Transportation: Take Tourist Shuttle Bus 810-1 or 810-2 to "Abu Oreum Entrance" stop.
"""

DOCUMENTS["24_geum_oreum_and_crater_lake.txt"] = """Title: Geum Oreum Sunset Peak and Crater Pond Guide
Source: Hallim-eup Administrative Center & VisitJeju
Access Date: 2026-10-20
Category: Volcanic Oreums & Sunset Views

Overview:
Geum Oreum (also called Geomun-oreum of the west, or Geumak Oreum) is located in Geumak-ri, Hallim-eup, rising to an elevation of 427.5 meters (relative height 178 meters). It is one of the very few volcanic oreums on Jeju Island outside of Mount Hallasan that features a permanent summit crater pond (known locally as "Wangmae").

Key Highlights and Activities:
1. The Summit Water Pond (Wangmae):
   - A circular volcanic depression at the summit measuring roughly 50 meters across. Depending on recent seasonal rainfall, it holds clear water that reflects the sky, white clouds, and mountain cows resting on the grassy banks.
2. Premier Western Sunset Lookout:
   - Faces directly toward the western ocean horizon, Biyangdo Island, and the coastal windmills of Sinchang.
   - Every clear evening, hundreds of travelers gather along the crater rim to watch the brilliant crimson sun set into the sea.
3. Paragliding Launch Center:
   - Due to optimal westerly updrafts, Geum Oreum is the premier paragliding hub on Jeju. Professional tandem flights take off directly from the northern crater ridge, gliding over Hallim plains and cattle pastures (flights approx. 120,000 KRW).

Access and Hiking Information:
- Paved Service Road: A winding concrete access road leads from the parking lot to the summit. Vehicle access is restricted to paragliding operators and authorized staff; visitors walk up the gentle 1.2-kilometer paved road (approx. 15 to 20 minutes).
- Admission: Free.
- Parking: Free paved parking lot at the base with restrooms and cafe trucks.
- Public Transit: Blue Bus 291 or 292 from Hallim Transfer Center to "Geumak-ri" stop, then walk 15 minutes to trailhead.
"""

DOCUMENTS["25_nokgame_and_baenyangi_oreums.txt"] = """Title: Noksan-ro Gasi-ri Oreums and Canola Plains
Source: Pyoseon-myeon Municipal Council & Gasi-ri Village Development Committee
Access Date: 2026-10-20
Category: Volcanic Oreums & Agricultural Heritage

Overview:
Situated in Gasi-ri, Pyoseon-myeon, the twin oreums of Nokgame (Big Deer Mountain, 474m) and Ttarabi Oreum (342m) anchor the pastoral heartland of historical Tamna horse breeding. The region is traversed by Noksan-ro, officially recognized by the Ministry of Land, Infrastructure and Transport as one of the "100 Most Beautiful Roads in Korea."

Seasonal Splendor and Geological Highlights:
1. Noksan-ro Canola and Cherry Blossom Corridor:
   - In early April, a 10-kilometer stretch of Noksan-ro road bursts into a dual bloom: vibrant yellow canola flowers line the road verges while overarching pink cherry blossom trees form a floral tunnel overhead.
2. Ttarabi Oreum ("King of Autumn Oreums"):
   - Features three overlapping craters and six graceful ridgeline knolls.
   - In October and November, its entire amphitheater is buried under dense, golden pampas grass waving beneath towering white wind turbines of the Gasi-ri Wind Farm.
3. Historical Royal Horse Ranch (Sanmapyeong):
   - During the Joseon Dynasty, the vast grasslands between Nokgame and Ttarabi served as the premier state-run horse ranch (Gammabang) breeding battle horses for the royal court.

Visitor Amenities and Trails:
- Well-marked walking circuits (Gasi-ri Jjolbun-gapma-jang-gil, a 10-km circular trekking route).
- Free public parking and trail markers.
- Transit: Take Blue Trunk Bus 221 or 222 to "Gasi-ri", then take Village Bus 732 to "Jeju Horse Park / Ttarabi".
"""

DOCUMENTS["26_saraoreum_hallasan_crater_lake.txt"] = """Title: Saraoreum Alpine Crater Lake Guide (Hallasan)
Source: Hallasan National Park Authority & Jeju World Heritage Office
Access Date: 2026-10-20
Category: Alpine Crater & National Park Trails

Overview:
Saraoreum is a parasitic volcanic cone located at an altitude of 1,324 meters on the northeastern flank of Mount Hallasan, accessible via a short spur branch off the Seongpanak Trail. Designated as Natural Monument No. 584, it is famous for housing the highest natural crater lake on Jeju Island outside of Baeknokdam summit.

Alpine Tarn and Wooden Boardwalk:
- The Summit Crater Lake (Sanam):
  - A magnificent circular crater tarn measuring 250 meters in diameter and roughly 100 meters across the water body.
  - After summer monsoon rains and autumn downpours, water fills the crater basin, submerging the wooden deck boardwalk so that hikers can walk literally barefoot or in water boots across the clear alpine pool.
- Observation Lookout Deck:
  - At the southern rim of Saraoreum, an elevated viewing platform overlooks Seogwipo city, the southern coastline, Munseom Island, and the soaring South Wall of Hallasan crater.

Access and Trail Rules:
- Route: Hikers must climb the Seongpanak Trail from Seongpanak Trailhead to the Saraoreum Junction (5.8 km, approx. 2 hours), then ascend the 600-meter wooden staircase spur to the crater lake (20 minutes).
- Hallasan Reservation Rules: Because Saraoreum lies on the lower section of the Seongpanak Trail prior to the Jindallaebat checkpoint, visitors who ONLY hike to Saraoreum and return down do NOT require a summit reservation permit. However, if continuing past Jindallaebat to the Baeknokdam summit, an official permit is mandatory.
- Gear: Sturdy trekking boots and windproof layers required; weather shifts rapidly at 1,300 meters.
"""

# ==============================================================================
# CATEGORY 4: WATERFALLS, VALLEYS & SPRINGS (27 - 32)
# ==============================================================================

DOCUMENTS["27_cheonjiyeon_waterfall_and_subtropical_forest.txt"] = """Title: Cheonjiyeon Waterfall and Subtropical Forest Guide
Source: Seogwipo City Tourism Department & Cultural Heritage Administration
Access Date: 2026-10-20
Category: Natural Monument & Waterfalls

Overview:
Cheonjiyeon Waterfall ("Pond of the Connection of Sky and Land") is situated in a deep, sheltered volcanic ravine in Cheonji-dong, Seogwipo City. The waterfall drops 22 meters down a vertical face of columnar basalt into an artificial natural plunge pool with a water depth of 20 meters. Designated as Natural Monument No. 379, the surrounding valley is a protected sanctuary for rare subtropical flora and fauna.

Unique Ecological and Night Features:
- Sanctuary of Wild Dampalsu Trees: The valley is the northernmost global habitat of the Elaeocarpus sylvestris (Dampalsu tree, Natural Monument No. 163). Dense groves of evergreen Castanopsis, Camellia japonica, and subtropical ferns line the canyon walls.
- Habitat of the Giant Mottled Eel: The deep, cool waters of Cheonjiyeon pool are home to the nocturnal Giant Mottled Eel (Anguilla marmorata, Natural Monument No. 258), which can grow up to 2 meters in length.
- Night Illumination: Unlike most natural attractions in South Korea, Cheonjiyeon is fully illuminated by warm golden lanterns and LED pathway lights until late evening (open until 22:00), making it the premier nighttime walking destination in Seogwipo.
- Barrier-Free Trail: The 1-kilometer pathway from the ticketing gate to the waterfall is completely paved with crushed basalt and flat cobblestones with zero staircases, making it 100% accessible to wheelchairs and baby strollers.

Operating Hours and Fees:
- Operating Hours: Daily 09:00 to 22:00 (last entry at 21:20). Open all 365 days.
- Admission Fees: Adults (ages 25-64): 2,000 KRW; Youth/Military: 1,000 KRW; Children (ages 7-12): 1,000 KRW; Seniors (65+) and infants: Free.
- Parking: Free municipal parking lot accommodating over 300 vehicles.

Transportation:
- Located within a 15-minute walk from Seogwipo Maeil Olle Market and Cheonjiyeon Port. Take Blue Bus 611, 612, or Airport Limousine 600 to "New Kyungnam Hotel" and walk 10 minutes down to the ravine.
"""

DOCUMENTS["28_jeongbang_waterfall_ocean_cascade.txt"] = """Title: Jeongbang Waterfall Direct Ocean Cascade Guide
Source: Seogwipo City Administration & Cultural Heritage Administration
Access Date: 2026-10-20
Category: Natural Monument & Scenic Waterfall

Overview:
Jeongbang Waterfall is situated in Donghong-dong, Seogwipo City. Dropping 23 meters from a vertical basalt sea cliff directly into the ocean surf, it is celebrated as the only natural coastal waterfall in Asia (and one of the few in the world) that discharges fresh river water directly into the sea. Designated as Scenic Site No. 43, it is historically ranked among the "Twelve Scenic Wonders of Yeongju" (Yeongju Sipgyeong).

Key Highlights and Folklore:
- Ocean Spray and Rainbows: As the mountain stream cascades off the cliff into the rocky ocean inlet, ocean breezes disperse fine mist across the boulder beach, frequently creating vivid rainbows in morning sunlight.
- Legend of Xu Fu (Seobul): According to ancient historical accounts, Xu Fu, the court envoy of Qin Shi Huang (First Emperor of China), was sent to Mount Hallasan (then called Mount Yeongju) in search of the elixir of immortality. On his return journey, he was enchanted by Jeongbang Waterfall and carved four Chinese characters ("Seobul Gwaji", meaning "Xu Fu passed by here") into the cliff face, from which the city name "Seogwipo" (meaning "Xu Fu's departure port") originated.
- Haenyeo Fresh Seafood Stalls: On the rocky boulder beach beside the waterfall basin, local female divers (Haenyeo) operate open-air mats serving freshly harvested live abalone, sea cucumber, sea squirts, and octopus sliced to order with spicy red pepper sauce.

Visiting Hours and Safety Information:
- Operating Hours: Daily 09:00 to 18:00 (last ticketing 17:30, seasonal adjustment in winter to 17:00).
- Admission Fees: Adults: 2,000 KRW; Youth/Children: 1,000 KRW.
- Access Stairs: Reached via a descent of 130 stone and wooden steps. The beach beneath the falls consists of large, slippery coastal basalt boulders; flat non-slip footwear is essential.
- Nearby Attraction: A 10-minute walk east leads to "Sojongbang Waterfall", a smaller 5-meter coastal cascade popular with locals for natural cold water massage in summer.

Transportation:
- From Seogwipo Intercity Bus Terminal, take City Bus 611, 612, or 641 to "Jeongbang Waterfall Entrance" stop.
"""

DOCUMENTS["29_cheonjeyeon_waterfall_three_tiers.txt"] = """Title: Cheonjeyeon Waterfall and Seonimgyo Bridge Guide
Source: Seogwipo City Tourism Bureau & Jungmun Tourism Complex
Access Date: 2026-10-20
Category: Natural Monument & Cultural Complex

Overview:
Cheonjeyeon Waterfall ("Pond of the Emperor of Heaven") is a magnificent three-tiered cascade located inside the Jungmun Tourist Complex in Seogwipo City. Fed by cold freshwater springs emerging from the foothills of Hallasan, the stream carves through a deep subtropical canyon before flowing into the Pacific Ocean.

The Three Cascade Stages:
1. First Waterfall (The Upper Falls):
   - A dramatic 22-meter cliff of columnar basalt framing a deep turquoise pond with a depth of 21 meters.
   - Flow: Only flows during and immediately following heavy rainfall; during dry weather, it exists as a tranquil, shimmering emerald pool surrounded by vertical rock columns.
2. Second Waterfall (The Main Falls):
   - Located 300 meters downstream from the first pool.
   - Flow: Flows continuously year-round, cascading down a picturesque 30-meter-wide stepped rock ledge surrounded by dense evergreen laurel forests.
3. Third Waterfall (The Lower Falls):
   - Located 500 meters further downstream, flowing through a deep ravine before joining the ocean at Seongcheon Port.

Seonimgyo Bridge ("Seven Nymphs Bridge"):
- An imposing, arched red-and-white pedestrian bridge spanning 128 meters across the deep gorge at a height of 50 meters.
- Sculpted on both sides of the bridge are 14 graceful stone statues depicting seven heavenly nymphs descending to play lutes and bathe in the crystal pool.
- Crossing the bridge offers panoramic views of Hallasan to the north and the Pacific Ocean to the south.

Visitor Hours, Fees, and Access:
- Operating Hours: 09:00 to 18:00 daily (last ticketing at 17:10).
- Admission Fees: Adults: 2,500 KRW; Youth/Military: 1,350 KRW; Children: 1,350 KRW.
- Walking Time: Touring all three waterfalls and crossing Seonimgyo bridge takes approximately 1 to 1.5 hours and involves multiple wooden staircases.
- Transportation: Take Airport Limousine Bus 600 to "Yeomiji Botanical Garden / Jungmun Resort Entrance", then walk 5 minutes.
"""

DOCUMENTS["30_wonang_falls_and_donnaeko_valley.txt"] = """Title: Donnaeko Valley and Wonang Falls Cooling Sanctuary
Source: Seogwipo City Environment Bureau & Donnaeko Recreation Center
Access Date: 2026-10-20
Category: Freshwater Valley & Summer Eco-Tourism

Overview:
Donnaeko Valley is a lush, forested volcanic ravine situated in Sanghyo-dong at the southern base of Mount Hallasan in Seogwipo City. Fed year-round by natural mountain meltwater and underground basalt spring water that maintains an icy temperature of 12°C to 14°C even in the peak of summer, it is celebrated as the premier natural cooling sanctuary on Jeju Island.

Key Features of Wonang Falls:
- The Twin Mandarin Duck Falls (Wonang Waterfall):
  - Located a 15-minute walk down a wooden boardwalk through evergreen oak and Japanese cedar forests from the Donnaeko entrance.
  - A 5-meter double cascade that pours into a deep, crystalline natural pool of luminous turquoise and sapphire water.
  - Named "Wonang" (Mandarin Duck) because the two identical streams pour side by side, symbolizing conjugal fidelity and love in Korean culture.
- The Icy Plunge Tradition:
  - During the dog days of summer (Sombok in July and August), locals visit Donnaeko to immerse themselves in the freezing pool water, believing that standing under the mountain cascade eases neuralgia, back pain, and summer heat exhaustion.

Facilities, Regulations, and Safety:
- Free Public Admission: There is no entrance fee to Donnaeko Valley or Wonang Falls.
- Eco-Sanctuary Protection: The water is a primary municipal drinking water source; washing with soap, cooking, leaving trash, and unauthorized night camping are strictly prohibited.
- Swimming Rules: Swimming in the Wonang Falls plunge pool is allowed during designated summer daytime hours under supervision by municipal safety lifeguards. Life vests are mandatory in deep sections (free rentals provided by civil rescue teams).
- Camping Ground: Donnaeko Free Camping Ground features tent wooden platforms, fresh tap water, and clean public restrooms.

Transit:
- Take Blue Trunk Bus 281 or 611/612 from Seogwipo Downtown to "Donnaeko Recreation Area" stop.
"""

DOCUMENTS["31_andeok_valley_gorge_and_evergreen_forest.txt"] = """Title: Andeok Valley Primeval Gorge and Prehistoric Sites
Source: Cultural Heritage Administration & Andeok-myeon Office
Access Date: 2026-10-20
Category: Natural Monument & Historic Valley

Overview:
Andeok Valley is a dramatic, hidden volcanic canyon situated in Gamsan-ri, Andeok-myeon, southwestern Jeju. Formed by the Changgochon river carving deeply through massive columnar basalt formations over hundreds of thousands of years, the ravine is protected as Natural Monument No. 377 for its exceptionally preserved primeval evergreen laurel forest.

Natural and Prehistoric Highlights:
1. Subtropical Evergreen Canopy:
   - The deep, shaded gorge creates a unique microclimate where sunlight filters through a canopy of over 300 rare plant species, including wild camellias, Machilus thunbergii, and lush carpets of Japanese felt ferns (Cyrtomium falcatum) hanging from vertical rock cliffs.
2. Prehistoric Rock Shelter Caves (Bawi-geuneul):
   - Along the stream bed lie natural basalt overhang caves where archaeological excavations uncovered stone tools, pottery shards, and shell middens dating from the Tamna Kingdom and Korean Bronze Age.
3. Historical Retreat of Scholar Kim Jeong-hui:
   - During his 8-year political exile in nearby Daejeong-eup (1840-1848), the renowned Joseon calligraphy master and scholar Kim Jeong-hui (Chusa) frequently visited Andeok Valley to contemplate nature, admire its cliffs, and find philosophical inspiration for his famous "Chusa" calligraphy style.

Visitor Information:
- Admission: Free public access year-round.
- Walking Path: A flat 1.0-km round-trip wooden deck trail borders the crystal-clear brook, making it an easy 30-minute tranquil stroll.
- Filming Spot: Popular backdrop for historical Korean television dramas including "Gu Family Book" and "Dae Jang Geum".
- Transportation: Take Blue Trunk Bus 202 or 282 to "Andeok Valley" stop.
"""

DOCUMENTS["32_soesokkak_estuary_and_wooden_boats.txt"] = """Title: Soesokkak Estuary and Traditional Boat Experience
Source: Seogwipo City Tourism Bureau & Hahyo Village Cooperative
Access Date: 2026-10-20
Category: Scenic Estuary & Maritime Leisure

Overview:
Soesokkak Estuary is situated in Hahyo-dong on the southeastern coast of Seogwipo City, where the freshwater stream Hyodoncheon terminates and merges with the open sea. In the native Jeju dialect, "Soe" means an ox, "So" means a deep water pool, and "Kkak" means the river mouth. Recognized as Scenic Site No. 78, Soesokkak is renowned for its sheer volcanic cliff canyon, lush pine overhangs, and hypnotic deep-emerald water.

Unique Water Activities:
1. Traditional Wooden Teu Raft:
   - A primitive, flat logging raft constructed from natural Korean pine poles, steered by a local village boatman who pulls along an overhead rope traversing the canyon while narrating folklore.
   - Highly stable and suitable for all ages (fee approx. 10,000 KRW for adults, 5,000 KRW for children; 30-minute ride).
2. Traditional Wooden Rowboats (Bae):
   - Two-person classic wooden dinghies that visitors paddle themselves up and down the sheltered 800-meter canyon gorge, passing under curious rock formations shaped like an owl, a lion, and a sleeping camel.
   - Fee: 20,000 KRW per boat (seats 2 adults).
3. Hahyo Black Sand Beach:
   - At the estuary mouth where the canyon opens to the Pacific Ocean lies a scenic black volcanic sand beach framing views of the distant Hallasan mountain.

Booking, Hours, and Operations:
- Operating Hours: Daily 09:00 to 18:00 (summer), 09:00 to 17:00 (winter).
- Ticketing: Highly popular with rapid sellouts during weekends and holidays; on-site morning ticket registration or advance online reservation through the Hahyo Village Cooperative is recommended.
- Free Walking Trail: Visitors who do not ride boats can walk the elevated wooden deck boardwalk lining the canyon clifftops free of charge.

Transportation:
- Take Blue Bus 623 or 624 from Seogwipo Downtown directly to "Soesokkak Entrance" stop.
"""

# ==============================================================================
# CATEGORY 5: SURROUNDING SUB-ISLANDS OF JEJU (33 - 37)
# ==============================================================================

DOCUMENTS["33_udo_island_cow_island_traveler_guide.txt"] = """Title: Udo Island (Cow Island) Complete Traveler and Ferry Guide
Source: Udo-myeon Administrative Office & Seongsan Port Maritime Authority
Access Date: 2026-10-20
Category: Sub-Islands & Maritime Tourism

Overview:
Lying 3.5 km off the eastern coast of Seongsan-eup, Udo Island is the largest subsidiary island belonging to Jeju Special Self-Governing Province, covering an area of 6.18 square kilometers with a population of approximately 1,800 residents. Viewed from the summit of Seongsan Ilchulbong, the island's elongated shape resembles a recumbent cow resting peacefully in the ocean, earning it the name "Cow Island."

The Eight Scenic Wonders of Udo (Udopagyeong):
1. Sanho Sand Beach (Seobinbaeksa):
   - Located on the west coast, this world-rare white beach consists not of crushed coral or sea shells, but of rhodoliths—calcified marine red algae nodules that grew offshore and were washed ashore (Natural Monument No. 438). The water glows in distinct tropical hues of aquamarine and deep navy.
2. Udobong Peak and Lighthouse Park:
   - The island's highest elevation (132 meters) at the southern tip, offering dizzying cliff drops, lush meadows where cows graze, and an international lighthouse theme park.
3. Geommeolle Black Beach and Cave of the Morning Dragon:
   - A dramatic dark volcanic cove underneath Udobong cliffs featuring sea caves that can be entered by foot during low spring tide (Dongan-gyeonggul).
4. Famous Agricultural Delicacy:
   - Udo is famous across Korea for its miniature peanuts (Ttang-kong), cultivated in nutrient-rich volcanic soil. Visitors should sample homemade Udo peanut soft-serve ice cream, peanut makgeolli, and peanut pastries sold across the island.

Ferry Operations, Vehicle Restrictions, and Local Mobility:
- Passenger Ferries: Depart every 30 minutes from Seongsan Port Passenger Terminal (Seongsan-po Hang) to Cheonjin Port or Haumokdong Port on Udo.
- Crossing Time: Approx. 15 minutes each way. Round-trip ferry fare (including municipal entry fee) is 10,500 KRW for adults. Valid passport or government ID is strictly required to board.
- Rental Car Ban: To prevent traffic gridlock and pollution, standard rental cars are strictly prohibited from boarding Udo ferries, EXCEPT for groups accompanied by elderly travelers (65+), infants under 6, pregnant women, or disabled passengers.
- Internal Island Mobility: Travelers explore via local electric mobility trikes (approx. 25,000 - 35,000 KRW for 2 hours), rental bicycles (10,000 KRW/day), or the convenient Udo Tour Shuttle Bus (6,000 KRW day-pass stopping at all major sights).
"""

DOCUMENTS["34_gapado_island_green_barley_and_flat_landscapes.txt"] = """Title: Gapado Island Green Barley and Low-Lying Landscapes
Source: Daejeong-eup Office & Gapado Village Fishery Cooperative
Access Date: 2026-10-20
Category: Sub-Islands & Seasonal Ecotourism

Overview:
Gapado Island is situated 5.5 km south of Unjin Port (Moseulpo) in southwestern Jeju, resting midway between mainland Jeju and southernmost Marado. With a surface area of 0.84 square kilometers and a highest natural elevation of only 20.5 meters above sea level, Gapado is celebrated as the flattest inhabited island in South Korea, offering uninterrupted horizons and panoramic views of Mount Sanbangsan, Songaksan, and Hallasan across the water.

Key Highlights and the Green Barley Festival:
1. Green Barley Wave Festival (Cheongbori Chukje):
   - Held annually from early April to mid-May, when over 600,000 square meters (60% of the island's total land area) is carpeted in lush, emerald green barley stalks.
   - Ocean breezes create undulating green waves across the flat fields, framed by traditional black basalt stone walls and the deep blue sea.
2. Walking and Cycling Paradise:
   - Because the island has virtually no hills or steep slopes, it is the premier cycling destination on Jeju. Flat seaside boardwalks and central paths traverse the island in an easy 1-to-2-hour walk or a 45-minute bicycle tour. Bicycle rental stalls near Sangdong Port charge 5,000 KRW for single bikes and 10,000 KRW for tandems.
3. Gapado Local Specialties:
   - Roasted green barley tea, barley misugaru grain powder, fresh sea mustard (Miyeok), and wild sea snails (Bomal) harvested by resident Haenyeo divers.

Ferry Logistics from Unjin Port:
- Ferries depart from Unjin Port in Moseulpo (Daejeong-eup) 5 to 7 times daily (more frequent during the April festival). Crossing time is approx. 10 to 15 minutes.
- Round-trip fare: 14,100 KRW for adults (photo ID required).
- Recommended stay time: 2 to 3 hours.
"""

DOCUMENTS["35_marado_island_southernmost_territory.txt"] = """Title: Marado Island Southernmost Point of Korea Guide
Source: Daejeong-eup Office & Cultural Heritage Administration
Access Date: 2026-10-20
Category: Natural Monument & Territorial Island

Overview:
Situated 11 km south of the Jeju mainland, Marado is an isolated, cliff-ringed basalt tableland that holds the profound geographic distinction of being the absolute southernmost point of the Republic of Korea (33° 06′ N latitude). Spanning just 0.3 square kilometers with a perimeter of 4.2 km, the entire island is designated as Natural Monument No. 423 to preserve its unique marine habitats and isolation.

Key Landmarks and Experiences:
1. The Southernmost Point Monument:
   - An iconic granite obelisk marking the exact geographic southern terminus of Korean territory, standing proudly on an open clifftop overlooking the boundless East China Sea.
2. Marado Lighthouse:
   - First illuminated in 1915, this historic lighthouse stands on the highest ridge (elevation 39m), guiding international commercial vessels transiting between Korea, China, and Japan. The courtyard features miniature replicas of world-famous lighthouses.
3. Marado Jajangmyeon Phenomenon:
   - Famous throughout South Korea due to a legendary 1990s television commercial ("Jajangmyeon delivery anywhere!"). The main village street features nearly a dozen competing noodle restaurants serving seafood black bean noodles topped with locally harvested seaweed (tot) and tender octopus.
4. Sheer Coastal Sea Cliffs and Sea Stacks:
   - The island has no beaches; instead, sheer vertical basalt cliffs drop 20 meters into crashing ocean waves with dramatic sea caverns (Gwangjang-gul) and famous sea fishing platforms for red sea bream.

Ferry Transport and Travel Guidelines:
- Passenger Ferries: Depart from Unjin Port (Moseulpo) and Songaksan Mountain Port.
- Crossing Time: Approx. 25 to 30 minutes each way across open sea swells.
- Round-Trip Ticket: 19,000 KRW for adults (must present passport or national ID).
- Walking Time: The perimeter trail takes approximately 1 to 1.5 hours to walk completely. There are no motor vehicles or bicycle rentals; all touring is done on foot.
"""

DOCUMENTS["36_biyangdo_island_hyeopjae_gem.txt"] = """Title: Biyangdo Island (Flying Island) Hallim Guide
Source: Hallim-eup Administrative Office & VisitJeju
Access Date: 2026-10-20
Category: Sub-Islands & Volcanic Geology

Overview:
Resting 1.5 km off the coast of Hallim Port in western Jeju, Biyangdo is a pristine volcanic island covering 0.5 square kilometers with a resident population of roughly 150 people. According to historical records in the Goryeo Dynasty chronicles, the island erupted and emerged from the ocean in the year 1002 AD, making it one of the youngest volcanic formations in South Korea. Its name "Biyangdo" translates poetically to "The Island that Flew Over."

Geological Formations and Trails:
1. Biyangbong Peak and Bamboo Grove:
   - The volcanic crater peak rises to an altitude of 114 meters. A 20-minute shaded walking path climbs through a dense tunnel of native dwarf bamboo (Sinjang-dae) to the historic white lighthouse at the summit, offering panoramic vistas of Hyeopjae Beach and Mount Hallasan.
2. Volcanic Hornito (Ae-gi-eop-eun-dol / Baby-Carrying Rock):
   - On the northern coastline stand unique volcanic chimneys called "Hornitos" (Natural Monument No. 439), hollow spires of basalt formed when escaping volcanic gases welded molten lava spatter into dramatic freestanding chimneys.
3. Geomungeodeul Wetland:
   - A brackish natural coastal saltwater marsh (Puldeung) on the southern coast where seawater filters in during high tide, providing habitat for rare migratory wading birds and wetland plants.

Ferry Schedule and Logistics:
- Passenger Ferry: Departs from Hallim Port Passenger Terminal (Hallim-po Hang) 4 times daily (09:00, 12:00, 14:00, 16:00).
- Crossing Duration: Only 15 minutes. Round-trip fare is 9,000 KRW for adults.
- Island Circuit: The flat paved perimeter road is 3.5 km long and can be walked in roughly 1 hour.
- Local Delicacy: Biyangdo Bomal Juk (freshly cooked sea snail rice porridge) and naturally dried sea urchin roe sold at the ferry pier.
"""

DOCUMENTS["37_chujado_islands_archipelago_getaway.txt"] = """Title: Chujado Archipelago and Fishing Island Guide
Source: Chuja-myeon Municipal Council & Jeju Port Maritime Authority
Access Date: 2026-10-20
Category: Sub-Islands & Maritime Archipelago

Overview:
Situated in the Jeju Strait roughly 45 km north of Jeju City and halfway to the Korean mainland, the Chujado Archipelago consists of 4 inhabited islands (Upper Chuja, Lower Chuja, Chupodo, and Hoenggando) and 38 uninhabited rocky islets. Politically part of Jeju Special Self-Governing Province but culturally and linguistically retaining close ties to Jeollanam-do, Chujado is renowned across Korea as a premier sanctuary for sea anglers, unspoiled coastal hiking, and yellow corvina fishing.

Key Highlights and Trails:
1. Jeju Olle Trail Route 18-1:
   - An adventurous 18.2-km hiking route traversing both Upper and Lower Chujado, connected by the Chuja Bridge.
   - Highlights include the Chujado Lighthouse Observation Tower, the scenic ridge of Navabawi Rock, and the martyr's shrine of Hwang Gyeong-han (historical Catholic persecution memorial).
2. Yellow Corvina Festival (Chuja Jogi Chukje):
   - Held annually in autumn (September/October) celebrating the island's world-famous yellow corvina (Jogi) and salted anchovy sauce (Chuja Aekjeot).
3. Sea Fishing Paradise:
   - Clean, swift currents create ideal feeding grounds for black porgy, red seabream, rock bream, and Spanish mackerel, attracting sport fishermen year-round.

Ferry Transport and Access:
- Car Ferry & Fast Catamaran: Departs daily from Jeju Port International Passenger Terminal (Terminal 2) and Haenam Usuyeong Port.
- Crossing Time: Approx. 1 hour by fast vessel (Queen Star 2) or 2 hours by car ferry (Songlim Blue).
- One-way fare: Approx. 13,000 to 20,000 KRW.
- Overnight Stay: Because ferries operate once or twice daily, visitors typically book a 1-night stay at local family guesthouses (Minbak) to complete Olle Route 18-1.
"""
print(f"Batch 2 compiled: {len(DOCUMENTS)} documents ready.")
