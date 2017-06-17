import itertools
import pytest
import main

#def test_update():         #Смотреть описание в гугл форме
#    config = {
#        'ginger': {
#            'django': 2,
#            'flask': 3,
#        },
#        'cucumber': {
#            'flask': 1,
#        },
#    }
#
#    main.update(config, 'pylons', 7)
#    assert config == {
#        'ginger': {
#            'django': 2,
#            'flask': 3,
#            'pylons': 1,
#        },
#        'cucumber': {
#            'flask': 1,
#            'pylons': 6,
#        },
#    }
def test_update():
    config = {
        'ginger': {
            'django': 2,
            'flask': 3,
        },
        'cucumber': {
            'flask': 1,
        },
    }

    main.update(config, 'pylons', 7)
    assert config == {
        'ginger': {
            'django': 2,
            'flask': 3,
            'pylons': 2,
        },
        'cucumber': {
            'flask': 1,
            'pylons': 5,
        },
    }

def test_initial():
    config = {
        'ginger': {},
        'cucumber': {},
    }

    main.update(config, 'flask', 3)
    main.update(config, 'django', 3)

    assert sum(config['ginger'].values()) == sum(config['cucumber'].values())
    assert sum(sum(x.values()) for x in config.values()) == 3+3

def test_initial_and_update():
    config = {
        'ginger': {
            'django': 2,
            'flask': 3,
        },
        'cucumber': {},
    }  
    main.update(config, 'pylons', 5)
    main.update(config, 'flask', 3)
    main.update(config, 'django', 3)    
    assert sum(config['ginger'].values()) == sum(config['cucumber'].values())
    assert sum(sum(x.values()) for x in config.values()) == 8+8
              
def test__initial_three_clasters():
    config = {
        'ginger': {},
        'cucumber': {},
        'tomato': {},
                    
    }  
    main.update(config, 'pylons', 10)
    main.update(config, 'flask', 3)
    main.update(config, 'django', 3)
    main.update(config, 'app', 8)        
    assert sum(config['ginger'].values()) == sum(config['cucumber'].values()) == sum(config['tomato'].values())
    assert sum(sum(x.values()) for x in config.values()) == 8+8+8

@pytest.mark.xfail(reason="Advanced test. Optional to implement")
def test_predictable_config():
    permutations = []
    services = [
        ('flask', 7),
        ('django', 13),
        ('pylons', 17)
    ]

    for permutation in itertools.permutations(services):
        config = {
            'ginger': {},
            'cucumber': {},
        }
        for svc, num in permutation:
            main.update(config, svc, num)
        assert sum(sum(x.values()) for x in config.values()) == 7+13+17
        permutations.append(config)

    assert all(p == permutations[0] for p in permutations[1:])