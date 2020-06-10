from enum import Enum
from abc import ABC, abstractmethod


class ByteOrder(Enum):
    """ The ByteOrder enum of serialized data
    """
    BigEndian = 0
    LittleEndian = 1


class FundamentalUnitDimension(Enum):
    """FundamentalUnitDimension are the fundamental units that can be combined to form all types of units.
    """

    Length = 0
    """Fundamental dimension for length."""

    Mass = 1
    """Fundamental dimension for mass."""

    Time = 2
    """Fundamental dimension for time."""

    ElectricCurrent = 3
    """Fundamental dimension for electric current."""

    Temperature = 4
    """Fundamental dimension for temperature."""

    AmountOfSubstance = 5
    """Fundamental dimension for amount of substance."""

    LuminousIntensity = 6
    """Fundamental dimension for luminous intensity."""

    Currency = 7
    """Fundamental dimension for currency."""


class IPropertyChanged(ABC):
    """IPropertyChanged interface is used to emit signal/event when a property of an object changes.
    """

    @abstractmethod
    def property_changed(self, property_name: str):
        """
        property_changed is called to emit signal/event when property of child class changes
        :param property_name: name of property modified
        """
        pass


class IDescription(IPropertyChanged, ABC):
    """IDescription interface class provides descriptive information
    on a HydroCouple object. An entity that is describable has a caption (title or heading)
    and a description. These are not to be used for identification (see IIdentity).
    """

    def caption(self) -> str:
        """
        :return: caption to describe object
        """
        pass

    def set_caption(self, caption: str):
        """Sets caption for the entity.

        :param caption: is a str representing the caption for the entity
        """
        pass

    def description(self) -> str:
        """Gets additional descriptive information for the entity.

        :return:
        """
        pass

    def set_description(self, description: str):
        """

        :param description:
        :return:
        """
        pass
