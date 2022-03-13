insert into currency_statistics.bank (id, full_name, short_name, description, url)
values
    (1, 'PrivatBank', NULL, NULL, 'https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5'),
    (2, 'Raiffeisen Bank Aval', NULL, NULL, 'https://www.aval.ua/documents/currencies/kursy-valiut-v-kasakh-viddilen-banku'),
    (3, 'UkrSibbank', NULL, NULL, 'https://my.ukrsibbank.com/ua/personal/'),
    (4, 'Kit Group', NULL, NULL, 'https://obmenka.od.ua/');

insert into currency_statistics.currency (international_name, current_name, description, is_enabled)
values ('USD', 'usd', null, true), ('EUR', 'eur', null, true), ('RUB', 'rub', null, true), ('RUB', 'rur', null, true);

insert into currency_statistics.parsers (bank_id, module_name, class_name)
values (1, 'private_bank_parser', 'PrivateBankParser'), (2, 'aval_bank_parser', 'RaiffeisenBankAvalParser'),
       (3, 'ukrsib_bank_parser', 'UkrSibBankParser'), (4, 'kit_group_parser', 'KiGroupParser');
