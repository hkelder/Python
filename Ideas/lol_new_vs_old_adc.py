# This program is to compare League of Legends patch 8.11 new ADC Attack Damage and Ratio with the old ones.

print("LoL ADC AD and AD Ratio comparison (pre-8.11 and 8.11)")
print("\n This program is to compare League of Legends patch 8.11 new ADC Attack Damage and Ratio with the old ones.")
print("\n And show you the old and new pure AD at level 18.")
adc_name = input("\nPlease tell me the ADC name: ")


def oldAdcAd():
    old_ad = float(input("Please enter the old ADC Attack Damage:"))
    return old_ad


def oldAdcRatio():
    old_ratio = float(input("And enter the old ADC Attack Damage Ratio:"))
    return old_ratio


def newAdcAd():
    new_ad = float(input("Please enter the new ADC Attack Damage:"))
    return new_ad


def newAdcRatio():
    new_ratio = float(input("And enter the new ADC Attack Damage Ratio:"))
    return new_ratio


def comparison(old_adc_ad, old_adc_ratio, new_adc_ad, new_adc_ratio):
    counter = 1
    while counter < 19:
        print("Level %.2f: " % counter + "%.2f vs " % old_adc_ad + "%.2f" % new_adc_ad)
        if old_adc_ad > new_adc_ad:
            old_adc_ad = old_adc_ad + old_adc_ratio
            new_adc_ad = new_adc_ad + new_adc_ratio
            counter += 1

        else:
            return (adc_name + " AD and Ratio will be better at level: %.2f" % counter +
                    "\n The new AD will be %.2f" % new_adc_ad + " versus the old AD at that level %.2f" % old_adc_ad)


def maximumAD(old_adc_ad, old_adc_ratio, new_adc_ad, new_adc_ratio):
    old_max_ad = old_adc_ad + (old_adc_ratio * 18)
    new_max_ad = new_adc_ad + (new_adc_ratio * 18)
    return (adc_name + " pure AD at level 18 was %.2f" % old_max_ad + " before 8.11\n Now it will be %.2f"
            % new_max_ad)


old_adc_ad = oldAdcAd()
old_adc_ratio = oldAdcRatio()
new_adc_ad = newAdcAd()
new_adc_ratio = newAdcRatio()

print('\n', comparison(old_adc_ad, old_adc_ratio, new_adc_ad, new_adc_ratio))
print('\n', maximumAD(old_adc_ad, old_adc_ratio, new_adc_ad, new_adc_ratio))
