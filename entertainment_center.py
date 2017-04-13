import media
import fresh_tomatoes

# listed below are my top 6 favorite movies
snowden = media.Movie("Snowden",
                      "A former CIA agent reveals to the world classified
                      information regarding illegal mass surveillance conducted
                      by the National Security Agency",
                      "http://t3.gstatic.com/images?q=tbn:ANd9GcR-_6a24Yow0h-l96G3H3mKpdhqA8RQpFY9Dyz4RguxJtmloK_O",  # noqa
                      "https://www.youtube.com/watch?v=QlSAiI3xMh4")

mean_girls = media.Movie("Mean Girls",
                        "A home schooled girl from Africa comes to high school
                         in America and enters 'Girl World'",
                        "https://upload.wikimedia.org/wikipedia/en/8/8f/Mean_Girls_movie.jpg",  # noqa
                        "https://www.youtube.com/watch?v=6YjSIvmNjT8")

rogue_one = media.Movie("Rogue One: A Star Wars Story",
                        "A vengeful young lady holds the key to destroying the
                        Empire's most powerful weapon, but in order to do so,
                        she must join forces with a spy and other
                        resistance fighters to steal plans for the Rebel
                        Alliance",
                        "https://upload.wikimedia.org/wikipedia/en/d/d4/Rogue_One%2C_A_Star_Wars_Story_poster.png",  # noqa
                        "https://www.youtube.com/watch?v=frdj1zb9sMY")

force_awakens = media.Movie("Star Wars: Episode VII The Force Awakens",
                            "A scavenger from the planet Jakku teams up with a
                            renegade storm trooper to help a droid carry
                            important information to the Resistance",
                            "https://upload.wikimedia.org/wikipedia/en/a/a2/Star_Wars_The_Force_Awakens_Theatrical_Poster.jpg",  # noqa
                            "https://www.youtube.com/watch?v=sGbxmsDFVnE")

spice_world = media.Movie("Spice World",
                          "A look into the life of the Spice Girls!",
                          "https://upload.wikimedia.org/wikipedia/en/7/7c/Spice_world.jpg",  # noqa
                          "https://www.youtube.com/watch?v=XbG8d7CM0IQ")

great_gatsby = media.Movie("The Great Gatsby",
                           "A mystery millionaire appears in West Egg and
                           throws lavish parties, but who is he?",
                           "http://t2.gstatic.com/images?q=tbn:ANd9GcRHjdRa754KlBw3wFJaa8pxGHbESpYGpN2Pt0A63Wgseu2f42Jd",  # noqa
                           "https://www.youtube.com/watch?v=rARN6agiW7o")

movies = [spice_world, mean_girls, snowden, force_awakens,
          rogue_one, great_gatsby]
fresh_tomatoes.open_movies_page(movies)

print (media.Movie.__doc__)
