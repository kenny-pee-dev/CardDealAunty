import requests
import pydash


MONEY_SMART_URL = "https://www.moneysmart.sg/credit-cards/api/listings?locale=en&category_slug=best-credit-cards&sort_by=recommended&sort_order=asc"
CAMPAIGN_KEYS = ['image', 'snippet_text', 'claim_start', 'claim_end', 'claim_form_link', 'terms_link', 'promotion_start', 'promotion_end', 'id']

def getMoneySmartCardDeals():
  card_deals = requests.get(MONEY_SMART_URL).json()['data']

  sanitized_card_deals = []

  for card_deal in card_deals:
    card_deal_object = {}
    card_deal_attributes = card_deal['attributes']
    if (card_deal_attributes['campaign']):
      card_deal_campaign = card_deal_attributes['campaign']
      sanitized_campaign = dict((k, card_deal_campaign[k]) for k in CAMPAIGN_KEYS if k in card_deal_campaign)

      card_deal_object['name'] = card_deal_attributes['name']
      card_deal_object['slug'] = card_deal_attributes['slug']
      card_deal_object['campaign'] = sanitized_campaign
      card_deal_object['gifts'] = card_deal_campaign['gift_set']['attributes']['gifts']

      sanitized_card_deals.append(card_deal_object)

  return sanitized_card_deals
