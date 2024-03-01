## checking if qtf works without passing pytest cache across workflow 

commit: https://github.com/softwareTestingResearch/demo/commit/dd1011700bb24e0a31c24331e3ff0245e54236f4
run: https://github.com/softwareTestingResearch/demo/actions/runs/8105271542
result: not working, tests run in default order

## checking if action/cache can pass the pytest cache and qtf works

### first time, e.g., no cache

commit: https://github.com/softwareTestingResearch/demo/commit/f550ca5bc5478b93f51732cab54a147fa14c58e9
run: https://github.com/softwareTestingResearch/demo/actions/runs/8105388459/job/22153638026

### second time, e.g., should be cache

commit: https://github.com/softwareTestingResearch/demo/commit/6e73910dffd08786a340ffd1207e33d709949e54
run: https://github.com/softwareTestingResearch/demo/actions/runs/8105441719

result: cache not found in second time, qtf fails


## check if action/cache can pass sample.txt

cache save success: https://github.com/softwareTestingResearch/demo/commit/11916563538f13cb03edfcd0dedbedd7de8964c2
run: https://github.com/softwareTestingResearch/demo/actions/runs/8105642215/job/22154285129

## find the path for pytest cache

success commit: https://github.com/softwareTestingResearch/demo/commit/1e7fb47eb1df3e6046351896ff823b9b88d3350d 
run: https://github.com/softwareTestingResearch/demo/actions/runs/8105814033/job/22154738939


## print pytest cache

commit: https://github.com/softwareTestingResearch/demo/commit/30b2ab7c5652ac88532f8534a2dbb931bf012f1f
run: https://github.com/softwareTestingResearch/demo/actions/runs/8105851271/job/22154843361

## save pytest cache
commit: https://github.com/softwareTestingResearch/demo/commit/395718f642e0e09dc0f3d3a7cbfc7a9f0f8d4ed0
run: https://github.com/softwareTestingResearch/demo/actions/runs/8105892884/job/22154949534

## always save pytest cache
commit: https://github.com/softwareTestingResearch/demo/commit/f38d058ed417704aa02f3d10ac2de6fc91763a0a
run: https://github.com/softwareTestingResearch/demo/actions/runs/8105909754/job/22154993686

Tips:
- update a cache: https://github.com/actions/cache/blob/main/tips-and-workarounds.md#update-a-cache
- auto-remove unaccessed cache in the past 7 days: https://docs.github.com/en/actions/using-workflows/caching-dependencies-to-speed-up-workflows#usage-limits-and-eviction-policy


result: successfully update cache, the num runs since fail is updated to 4, as below

commit: https://github.com/softwareTestingResearch/demo/commit/2274ab26973b5fe1f820783a823b13bcc10210e1
run: https://github.com/softwareTestingResearch/demo/actions/runs/8105987090/job/22155212923

## check if save cache proceed even if there's failed tests

commit: https://github.com/softwareTestingResearch/demo/commit/661a2638190b33852c1d0760bdcf8f1d3982239a
run: https://github.com/softwareTestingResearch/demo/actions/runs/8106015986/job/22155284956

result: failed tests prevent other steps

## check if save cache proceed even if there's failed tests with continue-on-error

commit: https://github.com/softwareTestingResearch/demo/commit/5d76e4b78b95f2c09d9d040f2c39c444f2d379cb
run: https://github.com/softwareTestingResearch/demo/actions/runs/8106076522

## check if save cache proceed even if there's failed tests with if always

commit: https://github.com/softwareTestingResearch/demo/commit/a92d91877039119a1c0a6976d5826befc26b5d41
run: https://github.com/softwareTestingResearch/demo/actions/runs/8106125506/job/22155544341
result: works, save cache anyway

## check if save cache proceed even if there's failed tests with if always and break cache to restore/save

round 1
commit: https://github.com/softwareTestingResearch/demo/commit/9d7dd3fbe8c11cfc2d762d24579b117a28fb7d20
run: https://github.com/softwareTestingResearch/demo/actions/runs/8106340982

round 2
commit: https://github.com/softwareTestingResearch/demo/commit/18a5e794f6b19b02631360d0946df5dc75eb75ba
run: https://github.com/softwareTestingResearch/demo/actions/runs/8106358852/job/22156147320

result: works, cache is saved even if tests failed, and cache from nearest prev workflow is passed to the current workflow


## check if weight 0-1-0 runs recently failed test first

commit: https://github.com/softwareTestingResearch/demo/commit/e8c7e1fe3eb838b00250c5a6b7caf8e3ba5312da
run: https://github.com/softwareTestingResearch/demo/actions/runs/8106385139/job/22156219730
result: yes


## check if caches per run instance is saved (py 3.9 vs py 3.10)

commit: https://github.com/softwareTestingResearch/demo/commit/25aec15fe1fb116388c6f520bd2011f154eec401
run: https://github.com/softwareTestingResearch/demo/actions/runs/8106575700/job/22156722276
result: yes, check test_random.py
