# define constants
from PIL import ImageFont, Image

from draw_table import draw_table

DEFAULT_WIDTH = 1290
DEFAULT_HEIGHT = 2796
DEFAULT_BG_COLOR = (60, 60, 60)  # dark grey
DEFAULT_TEXT_COLOR = (255, 255, 255)  # white
DEFAULT_FONT = ImageFont.truetype("fonts/arial.ttf", 80)


def create_image(table_data, output_path="lockscreen.png", width=DEFAULT_WIDTH, height=DEFAULT_HEIGHT,
                 bg_color=DEFAULT_BG_COLOR, text_color=DEFAULT_TEXT_COLOR, font=DEFAULT_FONT):
    """
    Create an image with the given table data and save it to the output path as a PNG file.
    :param table_data: list of 2-string tuples including a header row
    :param output_path: can be just a filename or a full path
    :param width: image width
    :param height: image height
    :param bg_color: background color as a 3-tuple of RGB values
    :param text_color: text color as a 3-tuple of RGB values
    :param font: font object
    :return:
    """
    image = Image.new("RGB", (width, height), color=bg_color)

    # table_image is the rendered table without margins
    table_image = draw_table(table_data, font=font, cell_pad=(20, 20), margin=(0, 0), align=["r", "l"],
                             colors={"bg": bg_color, "cell_bg": bg_color, "header_bg": bg_color, "font": text_color,
                                     "rowline": bg_color, "colline": bg_color}, )

    table_size_x, table_size_y = table_image.size
    table_position_x = int((width / 2) - (table_size_x / 2))
    table_position_y = int(height / 3)

    # paste the table into the image at the appropriate position
    image.paste(table_image, (table_position_x, table_position_y))

    # Save the image
    image.save(output_path)
