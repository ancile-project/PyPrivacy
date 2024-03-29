from __future__ import annotations
from abc import ABC, abstractmethod
from functools import lru_cache

from pyprivacy.primitives.policy_helpers.expressions.special.command import Command
from pyprivacy.primitives.policy_helpers.expressions import *


class BaseExpression(ABC):
    """
    An abstract class for all Policy expressions.
    It only has d_step, e_step, and simplify.
    """

    operation = None

    @abstractmethod
    @lru_cache(maxsize=1200)
    def d_step(self, command: Command, atoms) -> BaseExpression:
        pass

    @abstractmethod
    @lru_cache(maxsize=1200)
    def e_step(self, atoms) -> Constants:
        pass

    @abstractmethod
    @lru_cache(maxsize=1200)
    def simplify(self) -> BaseExpression:
        pass
