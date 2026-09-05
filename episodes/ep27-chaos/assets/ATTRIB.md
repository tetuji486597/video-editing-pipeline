# EP27 overlay assets -- what was actually used

Master sources and licences are in `episodes/ATTRIBUTIONS_EP27-29.md`; this file records
which files the EP27 compositions load and how they were prepared. Derived files live in
`assets/prepared/` and are copied into each `animations/<slot>/assets/`.

| used in | file | prepared from | preparation |
|---|---|---|---|
| slot_hook | `lamelo_1000.jpg` | `lamelo_ball_allstar2022.jpg` (CC BY 2.0, Erik Drost, Wikimedia Commons) | lanczos downscale to 1000px wide; cropped in CSS to a 200px circle sticker (head + torso) for the 6-7 pop |
| slot_hook, slot_build | `chaos_monkey_white.png` | `chaos_monkey_logo.png` (Apache 2.0, Netflix OSS, 225px black line art) | 4x lanczos upscale + RGB negate (alpha kept) so the real logo reads white on the Netflix-red badge |
| slot_hook, slot_build, slot_payoff | `chimpanzini_bananini_render.png` | shared_assets/brainrot (Steal a Brainrot fan-wiki game-model render) | as-is, transparent |
| slot_hook, slot_problem | `skibidi_toilet_transparent.png` | Skibidi Toilet fan-wiki render (DaFuq!?Boom!) | as-is, transparent |
| slot_problem | `tung_tung_tung_sahur_render.png` | Steal a Brainrot fan-wiki render (no bat) | as-is; the bat is a hand-drawn SVG in a rotated wrapper div |
| slot_problem | `cameraman_2x.png` | `cameraman_skibidi_normal_transparent.png` (Skibidi Toilet fan wiki, 263x434) | 2x lanczos upscale (526x868); used twice as the filming crowd |
| slot_problem, slot_payoff | `amongus_red_crewmate_transparent.png` | Innersloth sprite via the Among Us fan wiki (150x198) | as-is (the 1200x502 key art turned out to be opaque black, its colour-key crop was rejected) |
| slot_build | `kai_cenat_2025.jpg` | Wikimedia Commons, CC BY 3.0, ImDavisss Live stream still | as-is, cropped in CSS (object-fit cover) inside a rounded photo card |
| slot_new_component | `bombardiro_crocodilo_render.png` | Steal a Brainrot fan-wiki render (408x220) | as-is; flies across the box grid |

Not used: `trippi_troppi_render.png` (staged into slot_payoff/assets but dropped from the card
to keep it quiet), `tralalero_tralala_*`, `skibidi_toilet_vector_cc0.png`, `cameraman_gametoons_*`,
`cameraman_scientist_*`, `kai_cenat_2023.jpg`, `lamelo_ball_illawarra2019.jpg`, the `*_scene.png`
backups, `amongus_crewmates_space_transparent.png` (opaque, not actually transparent).

All other visuals (racks, cables, clocks, doors, beds, moai, chef hat, wrench, Ohio outline,
sparkles, bombs, cubes, goo) are hand-built SVG/CSS. No emoji anywhere.
