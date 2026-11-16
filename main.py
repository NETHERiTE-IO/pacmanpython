#map
tiles.set_current_tilemap(tilemap(
    """Level1"""))

#player
pacman = sprites.create(assets.image(
    """pacman"""), SpriteKind.player)
scaling.scale_to_pixels(pacman, 16, ScaleDirection.HORIZONTALLY, ScaleAnchor.MIDDLE)
scaling.scale_to_pixels(pacman, 16, ScaleDirection.VERTICALLY, ScaleAnchor.MIDDLE)
tiles.place_on_tile(pacman, tiles.get_tile_location(15, 15))

#music


#movement
controller.move_sprite(pacman)
positionx = pacman.x
positiony = pacman.y

#camara
scene.camera_follow_sprite(pacman)

#enemy
#ghostred(1)
ghost1 = sprites.create(assets.image(
    """ghostred"""), SpriteKind.enemy)
tiles.place_on_tile(ghost1, tiles.get_tile_location(1, 30))

#ghostblue(2)
ghost2 = sprites.create(assets.image(
    """ghostblue"""), SpriteKind.enemy)
tiles.place_on_tile(ghost2, tiles.get_tile_location(1, 1))

#ghostpink(3)
ghost3 = sprites.create(assets.image(
    """ghostpink"""), SpriteKind.enemy)
tiles.place_on_tile(ghost3, tiles.get_tile_location(30, 30))

#ghostorange(4)
ghost4 = sprites.create(assets.image(
    """ghostorange"""), SpriteKind.enemy)
tiles.place_on_tile(ghost4, tiles.get_tile_location(30, 1))

#health
info.set_life(3)
health = 0
def on_debounce():
    if health == 1:
        health - 1
timer.debounce("health", 500, on_debounce)
def on_life_zero():
    game.set_game_over_message(True, "GAME OVER!")
info.on_life_zero(on_life_zero)
def on_background4():
    def on_forever():
        if health == 0 and pacman.overlaps_with(ghost1) or pacman.overlaps_with(ghost2) or pacman.overlaps_with(ghost3) or pacman.overlaps_with(ghost4):
            health + 1
            info.change_life_by(-1)
    forever(on_forever)
timer.background(on_background4)
#points
pointvalue = 10
def on_background3():
    def on_forever():
        if pointvalue == 0:
            pointvalue = 20
    forever(on_forever)
timer.background(on_background3)
def on_background():
    def on_forever():
        if pointvalue > 0:
                pointvalue - 1
                coin = sprites.create(assets.image(
                    """coin"""), SpriteKind.food)
                tiles.place_on_random_tile(coin, assets.tile("""background"""))
    forever(on_forever)
timer.background(on_background)
def on_score():
    game.set_game_over_message(True, "Congratulations!")
info.on_score(100, on_score)
coin = sprites.create(assets.image(
   """coin"""), SpriteKind.food)
tiles.place_on_random_tile(coin, assets.tile("""background"""))
def on_background2():
    def on_forever():
        if pacman.overlaps_with(coin):
            sprites.destroy(coin)
            info.change_score_by(5)
    forever(on_forever)
timer.background(on_background2)



