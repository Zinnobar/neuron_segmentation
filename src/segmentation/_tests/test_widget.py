import segmentation
import pytest

# this is your plugin name declared in your napari.plugins entry point
MY_PLUGIN_NAME = "neuron_segmentation"
# the name of your widget(s)
MY_WIDGET_NAMES = ["Example QWidget", "Example Magic Widget","Example Function Widget"]


@pytest.mark.parametrize("widget_name", MY_WIDGET_NAMES)
def test_something_with_viewer(widget_name, make_napari_viewer):
    viewer = make_napari_viewer()
    num_dw = len(viewer.window._dock_widgets)
    viewer.window.add_plugin_dock_widget(
        plugin_name=MY_PLUGIN_NAME, widget_name=widget_name
    )
    assert len(viewer.window._dock_widgets) == num_dw + 1

