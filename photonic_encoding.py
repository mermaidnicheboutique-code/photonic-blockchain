#!/usr/bin/env python3
"""
Photonic Encoding - Luxbin Light Language for Blockchain Data
"""

import json
import numpy as np

LUXBIN_ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,!?;:-()[]{}@#$%^&*+=_~`<>\"'|\\"

class LuxbinEncoder:
    """Luxbin photonic encoding for blockchain data"""

    @staticmethod
    def encode_transaction(tx_data):
        """Encode transaction as photonic data"""
        # Convert transaction to JSON string
        tx_json = json.dumps(tx_data, sort_keys=True, default=str)

        # Create Luxbin encoding
        luxbin_code = ""
        for char in tx_json[:100]:  # Sample for encoding
            if char in LUXBIN_ALPHABET:
                luxbin_code += char

        # Calculate photonic wavelength
        wavelength = 400 + (len(luxbin_code) % 300)  # Visible spectrum

        return PhotonicData(luxbin_code, wavelength)

    @staticmethod
    def encode_block(block_data):
        """Encode block as photonic data"""
        block_json = json.dumps(block_data, sort_keys=True, default=str)
        luxbin_code = "".join(c for c in block_json if c in LUXBIN_ALPHABET)[:150]
        wavelength = 450 + (len(luxbin_code) % 250)

        return PhotonicData(luxbin_code, wavelength)

class PhotonicData:
    """Represents photonic encoded data"""

    def __init__(self, luxbin_code, wavelength):
        self.luxbin_code = luxbin_code
        self.wavelength = wavelength
        self.frequency = 3e8 / (wavelength * 1e-9)  # Hz
        self.energy = 1240 / wavelength  # eV

    def get_wavelength(self):
        """Get wavelength in nm"""
        return self.wavelength

    def get_photonic_info(self):
        """Get complete photonic information"""
        return {
            "luxbin_code": self.luxbin_code,
            "wavelength_nm": self.wavelength,
            "frequency_hz": self.frequency,
            "energy_ev": self.energy,
            "color_region": self.get_color_region()
        }

    def get_color_region(self):
        """Get color region of light spectrum"""
        if self.wavelength < 400:
            return "ultraviolet"
        elif self.wavelength < 450:
            return "violet"
        elif self.wavelength < 490:
            return "blue"
        elif self.wavelength < 570:
            return "green"
        elif self.wavelength < 590:
            return "yellow"
        elif self.wavelength < 620:
            return "orange"
        elif self.wavelength < 750:
            return "red"
        else:
            return "infrared"