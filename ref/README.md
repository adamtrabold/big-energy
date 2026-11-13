# Reference netlists (not vendored)

The simulations in `eng/sim/reference/` and `eng/sim/fold/` check our design against the CA-72 golden netlists, which are licensed under GPL-3 and used only as a reference.

    git clone https://github.com/idlefoundry/ca-72 ref/ca-72
    git -C ref/ca-72 checkout d268d22a0af63a881868968abe5442a43d544f9f   # the commit we used (2026-11-06)
