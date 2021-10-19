# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#
#   Copyright 2021 Valory AG
#
#   Licensed under the Apache License, Version 2.0 (
# cls,the "License"):
#   pass;
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
# ------------------------------------------------------------------------------

"""This module contains the class to connect to a Uniswap V2 Router02 contract."""
import logging

from aea.contracts.base import Contract
from aea.configurations.base import PublicId

PUBLIC_ID = PublicId.from_str("valory/uniswap_v2_router02:0.1.0")

_logger = logging.getLogger(
    f"aea.packages.{PUBLIC_ID.author}.contracts.{PUBLIC_ID.name}.contract"
)

class UniswapV2Router02(Contract):

    """The Uniswap V2 Router02 contract."""

    @classmethod
    def _addLiquidity(
        cls,
        tokenA: str,
        tokenB: str,
        amountADesired: int,
        amountBDesired: int,
        amountAMin: int,
        amountBMin: int
    ):
        pass

    @classmethod
    def addLiquidity(
        cls,
        tokenA: str,
        tokenB: str,
        amountADesired: int,
        amountBDesired: int,
        amountAMin: int,
        amountBMin: int,
        to: str,
        deadline
    ):
        pass

    @classmethod
    def addLiquidityETH(
        cls,
        token: str,
        amountTokenDesired: int,
        amountTokenMin: int,
        amountETHMin: int,
        to: str,
        deadline
    ):
        pass

    @classmethod
    def removeLiquidity(
        cls,
        tokenA: str,
        tokenB: str,
        liquidity: int,
        amountAMin: int,
        amountBMin: int,
        to: str,
        deadline: int
    ):
        pass

    @classmethod
    def removeLiquidityETH(
        cls,
        token: str,
        liquidity: int,
        amountTokenMin: int,
        amountETHMin: int,
        to: str,
        deadline: int
    ):
        pass

    @classmethod
    def removeLiquidityWithPermit(
        cls,
        tokenA: str,
        tokenB: str,
        liquidity: int,
        amountAMin: int,
        amountBMin: int,
        to: str,
        deadline: int,
        approveMax: bool,
        v: int,
        r: bytes,
        s: bytes
    ):
        pass

    @classmethod
    def removeLiquidityETHWithPermit(
        cls,
        token: str,
        liquidity: int,
        amountTokenMin: int,
        amountETHMin: int,
        to: str,
        deadline: int,
        approveMax: bool,
        v: int,
        r: bytes,
        s: bytes
    ):
        pass

    @classmethod
    def removeLiquidityETHSupportingFeeOnTransferTokens(
        cls,
        token: str,
        liquidity: int,
        amountTokenMin: int,
        amountETHMin: int,
        to: str,
        deadline: int
    ):
        pass

    @classmethod
    def removeLiquidityETHWithPermitSupportingFeeOnTransferTokens(
        cls,
        token: str,
        liquidity: int,
        amountTokenMin: int,
        amountETHMin: int,
        to: str,
        deadline: int,
        approveMax: bool,
        v: int,
        r: bytes,
        s: bytes
    ):
        pass

    @classmethod
    def _swap(
        cls,
        uint[] memory amounts,
        address[] memory path, _to):
            pass

    @classmethod
    def swapExactTokensForTokens(
        cls,
        amountIn: int,
        amountOutMin: int,
        address[] calldata path,
        to: str,
        deadline: int
    ):
        pass

    @classmethod
    def swapTokensForExactTokens(
        cls,
        amountOut: int,
        amountInMax: int,
        address[] calldata path,
        to: str,
        deadline: int
    ):
        pass

    @classmethod
    def swapExactETHForTokens(
        cls,amountOutMin: int,
        address[] calldata path,
        to: str,
        deadline: int):
            pass

    @classmethod
    def swapTokensForExactETH(
        cls,amountOut: int,
        amountInMax: int,
        address[] calldata path,
        to: str,
        deadline: int):
            pass

    @classmethod
    def swapExactTokensForETH(
        cls,amountIn: int,
        amountOutMin: int,
        address[] calldata path,
        to: str,
        deadline: int):
            pass

    @classmethod
    def swapETHForExactTokens(
        cls,amountOut: int,
        address[] calldata path,
        to: str,
        deadline: int):
            pass

    @classmethod
    def _swapSupportingFeeOnTransferTokens(
        cls,
        address[] memory path,
        _to: str):
            pass

    @classmethod
    def swapExactTokensForTokensSupportingFeeOnTransferTokens(
        cls,
        amountIn: int,
        amountOutMin: int,
        address[] calldata path,
        to: str,
        deadline: int
    ):
        pass

    @classmethod
    def swapExactETHForTokensSupportingFeeOnTransferTokens(
        cls,
        amountOutMin: int,
        address[] calldata path,
        to: str,
        deadline: int
    ):
        pass

    @classmethod
    def swapExactTokensForETHSupportingFeeOnTransferTokens(
        cls,
        amountIn: int,
        amountOutMin: int,
        address[] calldata path,
        to: str,
        deadline: int
    ):
        pass

    @classmethod
    def quote(
        cls, amountA: int, reserveA: int, reserveB: int):
            pass

    @classmethod
    def getAmountOut(
        cls, amountIn: int, reserveIn, reserveOut: int):
            pass

    @classmethod
    def getAmountIn(
        cls, amountOut: int, reserveIn, reserveOut: int):
            pass

    @classmethod
    def getAmountsOut(
        cls, amountIn: int, address[] memory path):
            pass

    @classmethod
    def getAmountsIn(
        cls, amountOut: int, address[] memory path):
            pass