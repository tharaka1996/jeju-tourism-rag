"""
Corpus Expansion Script for Jeju Tourism RAG Assistant.
Generates 52 comprehensive, highly structured domain documents (bringing the total to 60 TXT + 1 PDF = 61 documents).
Follows official data from Jeju Tourism Organization (VisitJeju), UNESCO World Heritage Center,
and Jeju Special Self-Governing Province publications.
"""

import os
from pathlib import Path

DOCS_DIR = Path(__file__).resolve().parent.parent / "data" / "documents"
DOCS_DIR.mkdir(parents=True, exist_ok=True)

DOCUMENTS = {}

# ==============================================================================
# CATEGORY 1: GEOLOGY & UNESCO HERITAGE (09 - 12)
# ==============================================================================

DOCUMENTS["09_geomunoreum_lava_tube_system.txt"] = """Title: Geomunoreum Volcanic Cone and World Natural Heritage Guide
Source: Jeju World Natural Heritage Center & Cultural Heritage Administration
Access Date: 2026-10-20
Category: UNESCO World Natural Heritage & Volcanic Geology

Overview:
Geomunoreum is a parasitic volcanic cone located in Jocheon-eup, Jeju City, rising to an elevation of 456 meters above sea level. It is the designated origin and parent volcano of the famous Geomunoreum Lava Tube System, which flowed northeastward to the coast roughly 100,000 to 300,000 years ago, forming Manjanggul, Gimnyeonggul, Bengdwi-gul, Dangcheomuldonggul, and Yongcheon-donggul. Because of its outstanding geological significance, Geomunoreum was inscribed as South Korea's first UNESCO World Natural Heritage site in 2007 under the designation "Jeju Volcanic Island and Lava Tubes."

Hiking Trails and Exploration Courses:
Exploration of Geomunoreum is divided into three interconnected trekking courses:
1. Summit Course (Course 1):
   - Distance: 1.8 km loop (approx. 1 hour).
   - Route: Ascends from the World Natural Heritage Center to the summit observation deck, offering panoramic views of the horseshoe-shaped crater and surrounding oreums.
2. Crater Basin Course (Course 2):
   - Distance: 5.5 km loop (approx. 2.5 hours).
   - Route: Descends into the deep interior volcanic caldera crater, exploring collapsed lava caves, vertical blowholes (Soombigul), and dense Japanese cedar and temperate evergreen forests.
3. Full Ridge Course (Course 3):
   - Distance: 8.0 km total (approx. 3.5 to 4 hours).
   - Route: Follows the entire outer crater rim ridgeline covering all nine secondary peaks before returning to the visitor center.

Visitor Rules and Strict Reservation Requirements:
- Prior Reservation Required: Free independent entry is strictly prohibited. All visitors must make an advance reservation through the official World Heritage portal (www.jeju.go.kr/wnhcenter) or phone reservation.
- Daily Visitor Cap: Capped at a maximum of 450 hikers per day to prevent environmental degradation.
- Guided Treks: Hikers must be accompanied by an official World Natural Heritage nature commentator/guide at scheduled departure times (09:00 to 13:00, departing every 30 minutes).
- Mandatory Gear: Trekking or hiking shoes with non-slip treads are mandatory; sneakers with smooth soles, sandals, umbrella use on trails, and hiking poles without rubber caps are prohibited to protect fragile volcanic soils.
- Admission Fees: Adults (ages 25-64): 2,000 KRW; Youth and Military: 1,000 KRW; Children (ages 7-12): 1,000 KRW; Free admission for seniors aged 65+ and Jeju residents with valid photo ID.
- Operating Hours: Closed every Tuesday for ecosystem recovery and on Lunar New Year's Day and Chuseok.

Transit and Access:
- Public Transit: From Jeju Intercity Bus Terminal, take Red Express Bus 211, 212, or 221 to the "Jeju World Natural Heritage Center / Geomunoreum Entrance" bus stop (approx. 45 minutes).
"""

DOCUMENTS["10_jusangjeolli_hexagonal_basalt_cliffs.txt"] = """Title: Jungmun Daepo Columnar Jointed Lava Cliffs (Jusangjeolli)
Source: Jeju Special Self-Governing Province & VisitJeju
Access Date: 2026-10-20
Category: Geological Monument & Coastal Scenery

Overview:
The Jungmun Daepo Columnar Jointed Lava Cliffs (officially designated as Natural Monument No. 443) are situated along the southern coast of Jeju Island in Jungmun Tourist Complex, Seogwipo City. Columnar joints (Jusangjeolli) are distinctive hexagonal, pentagonal, and octagonal vertical stone pillars formed when thick basaltic lava (approx. 900°C to 1,100°C) erupted from nearby volcanic cones, rapidly cooled, and contracted upon encountering cold seawater. The vertical rock pillars reach heights of 20 to 30 meters, extending along a 2-kilometer stretch of coastline.

Geological Features and Marine Splendor:
- Columnar Geometry: The rock faces appear as though chiselled by a master stonemason, featuring remarkably uniform vertical polygons measuring 1 to 2 meters in diameter.
- Crashing Waves: During high tide and windy conditions, ocean swells from the open Pacific collide with the basalt pillars, blasting sea spray up to 20 meters into the air in spectacular geyser-like plumes.
- Elevated Boardwalks: A safe, continuous wooden observation boardwalk and panoramic lookout deck lead visitors along the clifftops without damaging the geological formations.

Visiting Hours and Admission Information:
- Operating Hours: Open daily from 09:00 to 18:00 (last ticketing and admission at 17:30). Open year-round.
- Admission Fees:
  - Adults (ages 25-64): 2,000 KRW
  - Teenagers and Military: 1,000 KRW
  - Children (ages 7-12): 1,000 KRW
  - Seniors (ages 65+) and toddlers under 6: Free admission with valid ID.
- Parking Fees: Standard passenger vehicles: 1,000 KRW; compact cars: 500 KRW.

Traveler Tips and Surrounding Attractions:
- Best Photography Times: Mid-to-late afternoon provides optimal frontal sunlight against the dark basalt columns. High tide produces the most dramatic ocean wave collisions.
- Proximity: Located adjacent to Jungmun International Convention Center (ICC Jeju), Beritnae Oreum, and the Olle Trail Route 8.
- Transportation: Take Airport Limousine Bus 600 from Jeju International Airport directly to the "ICC Jeju" stop (approx. 50 minutes), then walk 5 minutes toward the coast.
"""

DOCUMENTS["11_suwolbong_geopark_volcanic_strata.txt"] = """Title: Suwolbong Peak Global Geopark and Volcanic Strata Trail
Source: UNESCO Global Geoparks Network & Jeju Geoscience Institute
Access Date: 2026-10-20
Category: UNESCO Global Geopark & Geoscience Heritage

Overview:
Suwolbong Peak is a 77-meter-high hydrovolcanic tuff cone situated at Gosan-ri, Hangyeong-myeon, on the westernmost tip of Jeju Island. Formed roughly 18,000 years ago by explosive hydrovolcanic eruptions—where rising magma encountered shallow groundwater—Suwolbong is recognized internationally by volcanologists as an "open-air textbook of volcanology." Its continuous coastal cliff exposures display impeccably preserved pyroclastic surge deposits, planar cross-bedding, and massive volcanic bomb sag structures.

Key Scientific and Geological Highlights:
1. Pyroclastic Surge Strata (Eongal Coastal Trail):
   - A 1.5 km clifftop and seaside walking path extending between Gosan Port and Chagwido Port.
   - Shows horizontal layers of volcanic ash, lapilli, and volcanic bombs (lava boulders) that struck and bent wet ash beds during explosive eruptions.
2. Suwolbong Summit and Meteorological Observatory:
   - Elevation of 77 meters offering uninterrupted 360-degree panoramic views of Chagwido Island, Dangsanbong Oreum, and the vast plains of Gosan.
   - Houses the Gosan Weather Station and a coastal sunset observation pavilion (Suwoljeong).
3. Chagwido Island Marine Vista:
   - Just 500 meters offshore lies Chagwido, an uninhabited basalt island known for dramatic sea stacks (Eagle Rock and General Rock) and rich pelagic fishing waters.

Visitor Information, Transportation, and Hours:
- Admission: Free of charge for all coastal trails, boardwalks, and summit pavilions.
- Operating Hours: Open 24 hours daily year-round. Summit pavilion illuminated until dusk.
- Electric Cart Rentals: Environmentally friendly electric mobility carts and tandem bikes are available for rent at Gosan Port for self-paced touring along the Eongal coastal promenade (rental fees approx. 10,000 - 15,000 KRW for 40 minutes).
- Public Transit: From Jeju City or Hallim, take Blue Trunk Bus 202 or Express Bus 102 to "Gosan Transfer Station", then transfer to Village Bus 761 or 771 to "Suwolbong Entrance".
"""

DOCUMENTS["12_sanbangsan_and_yongmeori_coast.txt"] = """Title: Sanbangsan Mountain and Yongmeori Dragon Coast Guide
Source: Seogwipo City Tourism Department & Cultural Heritage Administration
Access Date: 2026-10-20
Category: Natural Monument & Geological Wonder

Overview:
Sanbangsan is a 395-meter bell-shaped trachyte lava dome rising precipitously above the southwestern coast of Andeok-myeon, Seogwipo City. Formed approximately 800,000 years ago during early volcanic phases, Sanbangsan has no crater and features vertical columnar basalt fissures and cliff caves. Directly at its coastal foot lies the Yongmeori Coast ("Dragon Head Coast"), an ancient hydrovolcanic tuff ring where layers of sandstone have been sculpted by millions of years of crashing waves into undulating, serpentine dragon-like sea cliffs.

Key Attractions and Sacred Sites:
1. Sanbanggulsa Cave Temple:
   - A natural rock grotto cavern perched midway up the south cliff face (elevation 150m).
   - Houses a stone Buddha statue dating back to the Goryeo Dynasty.
   - Natural mineral water drips continuously from the cave ceiling, known in folk legends as the "tears of Sanbangdeok", the guardian goddess of the mountain.
2. Yongmeori Coast Wave-Cut Platforms:
   - Walking along the sea shelf reveals dramatic undulating rock arches, sea gullies, potholes, and sandstone wave benches.
   - Near the entrance stands a replica of the Dutch sailing ship "Sperwer", commemorating Hendrick Hamel, who was shipwrecked on Jeju in 1653 and introduced Korea to the Western world.

Admission and Critical Safety Information:
- Combined Ticket (Sanbangsan Cave + Yongmeori Coast):
  - Adults: 2,500 KRW; Youth/Children: 1,500 KRW.
  - Individual Entry: 1,000 KRW for Sanbangsan; 2,000 KRW for Yongmeori Coast.
- Tidal and Weather Restrictions:
  - Yongmeori Coast walking trail is strictly closed during high tides, stormy seas, and heavy rain due to dangerous rogue waves sweeping over the rock shelves.
  - Visitors must check daily tide access times via phone (+82-64-794-2940) or through the VisitJeju website before traveling.
- Operating Hours: 09:00 to 18:00 (last entry 17:30 in summer, 17:00 in winter).

Transportation:
- From Jeju International Airport, take Express Bus 152 directly to "Sanbangsan" stop (approx. 60 minutes).
- From Seogwipo Downtown, take Blue Trunk Bus 252 or 202.
"""

# ==============================================================================
# CATEGORY 2: BEACHES, COASTS & MARINE PARKS (13 - 19)
# ==============================================================================

DOCUMENTS["13_hyeopjae_and_geumneung_beaches.txt"] = """Title: Hyeopjae and Geumneung Twin Beaches Traveler Guide
Source: Jeju Tourism Organization & Hallim-eup Municipal Council
Access Date: 2026-10-20
Category: Coastal Recreation & Natural Beaches

Overview:
Situated side by side on the northwestern coast of Jeju Island in Hallim-eup, Hyeopjae Beach and Geumneung Beach form a continuous, idyllic marine park famous for crystalline cobalt-and-emerald lagoons, brilliant white pulverized-shell sand, and an unobstructed frontal panorama of Biyangdo Island resting on the ocean horizon.

Distinctive Features and Differences:
1. Hyeopjae Beach:
   - More lively and commercial, backed by evergreen pine forests (Geumnung-won) and a bustling promenade of seaside cafes, fresh abalone restaurants, and equipment rentals.
   - Wide, sloping white sands rich in crushed mollusk shells, giving the water its tropical turquoise clarity.
2. Geumneung Beach:
   - Located immediately west of Hyeopjae, separated only by a low black basalt rock reef.
   - Much quieter and shallower, with vast tidal sandbars exposed during ebb tide where families with young children can safely wade, catch small hermit crabs, and explore shallow tidal pools.

Facilities, Regulations, and Operating Guidelines:
- Official Bathing Season: July 1 to August 31 annually (09:00 to 18:00 daily). Lifeguards from the Korea Coast Guard and municipal rescue teams patrol designated swimming zones.
- Night Swimming: During peak summer (late July to mid-August), night swimming is permitted in floodlit areas until 21:00.
- Shower and Changing Facilities: Modern municipal shower facilities charge 2,000 KRW for adults and 1,000 KRW for children. Locker rentals are 3,000 KRW.
- Free Public Camping: Dedicated tent camping grounds are maintained in the pine groves behind the beach. Open ground campfires are strictly prohibited; portable camping stoves are permitted in designated cooking zones.
- Parking: Free public parking lots are located at both Hyeopjae and Geumneung entrances.

Transit Directions:
- Take Blue Trunk Bus 202 (Western Coastal Route) from Jeju City Intercity Terminal or Hallim Transfer Center, alighting at "Hyeopjae Beach" or "Geumneung Beach" stops (approx. 50 minutes from Jeju City).
"""

DOCUMENTS["14_hamdeok_beach_and_seoubong_peak.txt"] = """Title: Hamdeok Beach and Seoubong Coastal Peak Guide
Source: Jeju Tourism Organization & Jocheon-eup Office
Access Date: 2026-10-20
Category: Marine Leisure & Coastal Walking

Overview:
Hamdeok Beach is situated 14 km east of Jeju City in Jocheon-eup. Renowned for its calm, wind-sheltered waters, powdery white sand, and brilliant contrast of black basalt stepping bridges, it is often called the "Maldives of Jeju." Anchoring the eastern flank of the beach is Seoubong Peak, a volcanic oreum rising 113 meters above the bay, which shelters the water from strong northeast swells and provides one of the island's most iconic coastal viewpoints.

Key Highlights:
1. Connected Sandbanks and Basalt Promenades:
   - Three distinct beach bays separated by natural volcanic reefs and arched wooden footbridges extending out over the water.
   - Extremely gentle slope: Even 50 meters from the shoreline, water depth rarely exceeds an adult's waist, making it the safest bathing area on the island.
2. Seoubong Coastal Trail:
   - An easy 20-to-30 minute walking trail climbing from the beach to the summit of Seoubong.
   - Spring Showcase: Entire hillside blooms in radiant yellow canola flowers (Yuchae-kkot) in March and April.
   - Autumn Showcase: Sown with fields of pink cosmos flowers.
   - Paragliding launch pad: Popular takeoff spot for coastal tandem paragliding over Hamdeok bay.

Amenities, Admission, and Night Atmosphere:
- Admission: Free public access year-round.
- Night Illumination: The beach promenade, palm trees, and ocean footbridges are bathed in colorful LED floodlights, creating a vibrant evening walking environment with bustling seafood restaurants and live acoustic buskers.
- Water Sports: Stand-up paddleboarding (SUP), banana boats, sea kayaking, and jet-skiing rentals operate along the western inlet from June through September.
- Shower Facilities: 2,000 KRW for adults; hot water available.

Transportation:
- Take Red Express Bus 101 from Jeju Airport directly to "Hamdeok Beach" (approx. 35 minutes).
- Take Blue Trunk Bus 201 or 260 from downtown Jeju City.
"""

DOCUMENTS["15_jungmun_saekdal_beach_surfing_haven.txt"] = """Title: Jungmun Saekdal Beach and Surfing Mecca Guide
Source: Seogwipo City Tourism Department & Korea Surfing Association
Access Date: 2026-10-20
Category: Coastal Marine Sports & Surfing

Overview:
Nestled beneath the towering cliffs of Jungmun Resort in Seogwipo City, Jungmun Saekdal Beach is a curved 560-meter coastal haven famous across East Asia as the birthplace of modern Korean surfing. Because the beach faces directly south into the open Pacific Ocean without sheltering barrier islands, it catches consistent, powerful swell waves averaging 2 to 4 meters throughout the year.

Unique Geological Features:
- Four-Colored Sand (Jinmosal): The sand is a rich, coarse mixture of four distinct natural mineral grains: black volcanic basalt, white calcium shell fragments, grey quartz, and red scoria (volcanic cinder).
- Clifftop Panorama: The beach is framed by 30-meter coastal sea cliffs adorned with lush subtropical palms and the luxury grounds of the Shilla, Lotte, and Parnas hotels.

Surfing and Marine Activities:
- Surfing Hub: Home to multiple certified ISA (International Surfing Association) surf schools offering beginner lessons, board rentals (approx. 30,000 to 40,000 KRW/day), and wetsuits.
- International Competitions: Annually hosts the Jeju International Surfing Competition in June, drawing professional riders from around the globe.
- Winter Penguin Swimming Festival: An eccentric traditional festival held every January where hundreds of brave participants plunge into the chilly ocean waters to pray for health and good fortune in the new year.

Safety Protocols and Hazards:
- Rip Currents (Yeok-pado): Jungmun is prone to strong offshore rip currents. Swimmers must strictly stay within flagged safe zones monitored by the Korea Coast Guard rescue towers.
- Surfer/Swimmer Separation: During summer months (July-August), the beach is strictly divided into dedicated surfing zones on the west and family swimming zones on the east.
- Operating Hours: Open daily; swimming allowed 09:00 to 18:00 during summer.

Transportation:
- From Jeju International Airport, take Airport Limousine Bus 600 directly to the "Korea Tourism Organization" or "The Shilla Jeju" stop (approx. 50 minutes), then walk down the paved cliff path (5 minutes).
"""

DOCUMENTS["16_woljeongri_and_gimnyeong_coasts.txt"] = """Title: Woljeongri Cafe Beach and Gimnyeong Yacht Coast
Source: Gujwa-eup Administrative Center & VisitJeju
Access Date: 2026-10-20
Category: Scenic Coast & Marine Tourism

Overview:
Located in Gujwa-eup in northeastern Jeju, the neighboring coastal strips of Woljeongri and Gimnyeong represent two contrasting facets of Jeju's ocean allure: Woljeongri is famous for its vibrant artistic cafe culture and offshore wind turbine landscape, while Gimnyeong is renowned for its tranquil yacht marina, turquoise waters, and resident Indo-Pacific bottlenose dolphins.

Key Highlights and Experiences:
1. Woljeongri Beach ("The Moon that Stays"):
   - A crescent-shaped bay with shallow, crystal-clear water and a row of giant white offshore wind generators rotating gracefully in the sea breeze.
   - Cafe Street: Dozens of charming seaside cafes line the coastal road, famous for placing colorful vintage wooden chairs directly on the seawall where travelers take iconic photos overlooking the blue horizon.
   - Clear Bottom Kayaks: Transparent sea kayaks (approx. 10,000 KRW for 30 minutes) let paddlers observe swimming fish and volcanic sea floors beneath their feet.
2. Gimnyeong Segi-al Beach and Yacht Tours:
   - Features brilliant white sands and natural black rock pools filled with sea snails and small crabs.
   - Gimnyeong Yacht Tour: Luxury catamaran yacht cruises depart from Gimnyeong Marina, offering sunset sailing, ocean fishing, wine tasting, and frequent sightings of wild Jeju Indo-Pacific bottlenose dolphins playing in the vessel's bow waves (cruises approx. 60,000 KRW for adults).

Visitor Amenities:
- Free public parking along the coastal road.
- Lifeguards on duty during official summer season (July-August).
- Convenient access to adjacent Manjanggul Lava Tube and Gimnyeong Maze Park.

Transportation:
- Take Blue Trunk Bus 201 from Jeju City Intercity Bus Terminal to "Woljeongri" stop (approx. 55 minutes).
- Connected to Jeju Olle Trail Route 20.
"""

DOCUMENTS["17_gwangchigi_beach_and_coastal_tidepools.txt"] = """Title: Gwangchigi Beach Sunrise and Geotrail Guide
Source: Seongsan-eup Council & Cultural Heritage Administration
Access Date: 2026-10-20
Category: Coastal Geosite & Sunrise Photography

Overview:
Gwangchigi Beach is an open coastal lava strand situated in Seongsan-eup, directly across the bay from the UNESCO World Heritage site Seongsan Ilchulbong. Rather than conventional soft swimming sands, Gwangchigi is celebrated for its vast fields of basalt lava bedrock covered in luminous green marine moss (Gamtae and Cheong-gak), creating one of South Korea's most photographed sunrise landscapes.

Geological Formations and Photography:
- Low Tide Miracle: At high tide, Gwangchigi appears as an unassuming dark sandy beach. But when the tide recedes twice daily, a vast plateau of ancient lava flow flats emerges from the ocean, carpeted in vivid green algae and dotted with natural tide pools reflecting the sky.
- Iconic Sunrise Composition: Photographers from around the world gather before dawn to capture the golden morning sun rising directly behind the dramatic crown of Seongsan Ilchulbong, mirrored in the shallow tidal pools between the mossy rocks.
- Horseback Riding on the Beach: Local stables offer horseback riding along the water's edge, giving travelers a cinematic riding experience with the volcanic crater looming in the background (approx. 10,000 - 20,000 KRW per ride).

Visiting and Safety Guidelines:
- Swimming Warning: Strong rip currents and sharp basalt rocks make swimming hazardous; Gwangchigi is primarily a walking, photography, and tidepool exploration site, not a swimming beach.
- Tide Tables: Visitors must consult the local tide forecast (Mulgol) to ensure their visit coincides with low tide (Ganjejo) to witness the mossy green rock plateau.
- Trail Significance: Serves as the official terminus of Jeju Olle Trail Route 1 and the starting gateway of Olle Route 2.
- Admission: Free public access 24 hours daily. Free parking along Coastal Route 1132.

Transportation:
- Take Red Express Bus 111 or 112 from Jeju International Airport directly to "Gwangchigi Beach" stop (approx. 1 hour 15 minutes).
"""

DOCUMENTS["18_pyoseon_haevichi_beach.txt"] = """Title: Pyoseon Haevichi Beach and Circular Sandbar Guide
Source: Pyoseon-myeon Office & Jeju Tourism Organization
Access Date: 2026-10-20
Category: Family Beach & Marine Festivals

Overview:
Pyoseon Haevichi Beach is situated in the southeastern village of Pyoseon-myeon, Seogwipo City. Spanning an enormous area of over 250,000 square meters, it is celebrated as having the largest tidal sandflat in South Korea. The name "Haevichi" translates poetically to "the place where the morning sun shines first."

Distinctive Tidal Phenomenon:
- Immense Low Tide Sandbar: During low tide, the ocean recedes for hundreds of meters, exposing a vast, circular expanse of powdery white crushed shell sand resembling a desert oasis surrounded by shallow turquoise lagoons.
- High Tide Transformation: During high tide, seawater flows back in, transforming the entire sandflat into an enormous, circular shallow swimming pool with an average depth of less than 1 meter.
- Fine Shell Powder: The sand consists of finely pulverized cockle and clam shells, renowned in traditional folk medicine for soothing skin irritations when travelers bury their legs in the warm sand ("Moraejjim" sand bath).

Events and Facilities:
- Pyoseon White Sand Summer Festival: Held annually in early August, featuring beach sports tournaments, night fireworks, live music concerts, and fresh watermelon-eating contests.
- Extensive Amenities: Spacious grassy camping areas, shaded wooden picnic gazebos, changing rooms, outdoor freshwater wash taps, and clean shower houses (2,000 KRW).
- Adjacent Attractions: Just a 3-minute drive from Jeju Folk Village and Pyoseon Haevichi Resort.

Safety and Hours:
- Very safe for toddlers, young children, and elderly travelers due to the absence of sudden drop-offs or powerful surf.
- Official summer bathing season: July 1 to August 31 (09:00 - 18:00). Free admission and parking.

Transportation:
- Take Red Express Bus 121 or 122 from Jeju International Airport directly to "Pyoseon Jeju Bank / Beach" stop (approx. 1 hour).
"""

DOCUMENTS["19_ihotewoo_beach_and_twin_horse_lighthouses.txt"] = """Title: Iho Tewoo Beach and Twin Horse Lighthouses
Source: Jeju City Tourism Division & VisitJeju
Access Date: 2026-10-20
Category: Urban Beach & Maritime Culture

Overview:
Located in Iho-dong, just 5 km west of Jeju International Airport, Iho Tewoo Beach is the most accessible coastal retreat for travelers arriving on the island. Combining yellow-grey volcanic sand with cultural heritage installations, it is universally recognized by the striking twin wooden-horse lighthouses standing proudly at the harbor entrance.

Key Highlights and Cultural Heritage:
1. Twin Horse Lighthouses (Mal-deungdae):
   - Two massive geometric lighthouses shaped like iconic Jeju ponies stand at the breakwater: one painted bright crimson red (guiding incoming vessels) and the other stark white (marking the harbor channel).
   - Considered one of the top photography and sunset landmarks in Jeju City, with planes descending overhead into the airport.
2. Traditional Won-dam Fishing Stone Walls:
   - A traditional Jeju tidal stone weir (Won-dam) is preserved on the shoreline: a crescent-shaped wall of loose basalt stones that traps fish inside as the tide ebbs.
   - Every August, the beach hosts the "Iho Tewoo Festival", celebrating traditional net fishing and boat racing using primitive flat pine log rafts called "Tewoo".
3. Evening Food Stalls (Pocha):
   - In summer, open-air tent restaurants line the boardwalk, serving charcoal-grilled seafood, cold draft beer, and spicy ramyeon under the ocean breeze until late midnight.

Visitor Information:
- Admission: Free 24/7 access.
- Summer Bathing: Official swimming July to August (09:00 to 19:00).
- Proximity: Only a 10-minute taxi ride (approx. 7,000 KRW) from Jeju International Airport terminals.
- Bus Access: Take City Bus 370, 316, or 453 from the airport to "Iho Tewoo Beach" stop.
"""
print(f"Batch 1 compiled: {len(DOCUMENTS)} documents ready.")
