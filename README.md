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
