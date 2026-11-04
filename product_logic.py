from digital_product import DigitalProduct
from physical_product import PhysicalProduct

PRODUCT_TYPES = {
    PhysicalProduct.TYPE: PhysicalProduct,
    DigitalProduct.TYPE: DigitalProduct,
}

# Old saved records may not have a type field, 
# this gives them a default type of PhysicalProduct
DEFAULT_TYPE = PhysicalProduct.TYPE


def product_from_dict(data):
    product_type = data.get("type", DEFAULT_TYPE)
    product_class = PRODUCT_TYPES.get(product_type)
    if product_class is None:
        raise ValueError(f"Unknown product type: {product_type}")
    return product_class.from_dict(data)