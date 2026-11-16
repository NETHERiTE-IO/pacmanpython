// map
tiles.setCurrentTilemap(tilemap`Level1`)
// player
let pacman = sprites.create(assets.image`pacman`, SpriteKind.Player)
scaling.scaleToPixels(pacman, 16, ScaleDirection.Horizontally, ScaleAnchor.Middle)
scaling.scaleToPixels(pacman, 16, ScaleDirection.Vertically, ScaleAnchor.Middle)
tiles.placeOnTile(pacman, tiles.getTileLocation(15, 15))
// music
// movement
controller.moveSprite(pacman)
let positionx = pacman.x
let positiony = pacman.y
// camara
scene.cameraFollowSprite(pacman)
// enemy
// ghostred(1)
let ghost1 = sprites.create(assets.image`ghostred`, SpriteKind.Enemy)
tiles.placeOnTile(ghost1, tiles.getTileLocation(1, 30))
// ghostblue(2)
let ghost2 = sprites.create(assets.image`ghostblue`, SpriteKind.Enemy)
tiles.placeOnTile(ghost2, tiles.getTileLocation(1, 1))
// ghostpink(3)
let ghost3 = sprites.create(assets.image`ghostpink`, SpriteKind.Enemy)
tiles.placeOnTile(ghost3, tiles.getTileLocation(30, 30))
// ghostorange(4)
let ghost4 = sprites.create(assets.image`ghostorange`, SpriteKind.Enemy)
tiles.placeOnTile(ghost4, tiles.getTileLocation(30, 1))
// health
info.setLife(3)
let health = 0
timer.debounce("health", 500, function on_debounce() {
    if (health == 1) {
        health - 1
    }
    
})
info.onLifeZero(function on_life_zero() {
    game.setGameOverMessage(true, "GAME OVER!")
})
timer.background(function on_background4() {
    forever(function on_forever() {
        if (health == 0 && pacman.overlapsWith(ghost1) || pacman.overlapsWith(ghost2) || pacman.overlapsWith(ghost3) || pacman.overlapsWith(ghost4)) {
            health + 1
            info.changeLifeBy(-1)
        }
        
    })
})
// points
let pointvalue = 10
timer.background(function on_background3() {
    forever(function on_forever() {
        let pointvalue: number;
        if (pointvalue == 0) {
            pointvalue = 20
        }
        
    })
})
timer.background(function on_background() {
    forever(function on_forever() {
        let coin: Sprite;
        if (pointvalue > 0) {
            pointvalue - 1
            coin = sprites.create(assets.image`coin`, SpriteKind.Food)
            tiles.placeOnRandomTile(coin, assets.tile`background`)
        }
        
    })
})
info.onScore(100, function on_score() {
    game.setGameOverMessage(true, "Congratulations!")
})
let coin = sprites.create(assets.image`coin`, SpriteKind.Food)
tiles.placeOnRandomTile(coin, assets.tile`background`)
timer.background(function on_background2() {
    forever(function on_forever() {
        if (pacman.overlapsWith(coin)) {
            sprites.destroy(coin)
            info.changeScoreBy(5)
        }
        
    })
})
