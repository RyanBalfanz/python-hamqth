class SessionIDRequestResponse:
    text = """
    <?xml version="1.0"?>
    <HamQTH version="2.7" xmlns="https://www.hamqth.com">
    <session>
    <session_id>09b0ae90050be03c452ad235a1f2915ad684393c</session_id>
    </session>
    </HamQTH>
    """.strip()


class SessionIDRequestFailedResponse:
    text = """
    <?xml version="1.0"?>
    <HamQTH version="2.7" xmlns="https://www.hamqth.com">
    <session>
    <error>Wrong user name or password</error>
    </session> 
    </HamQTH>
    """.strip()


class SearchCallsignResponse:
    text = """
    <?xml version="1.0"?>
    <HamQTH version="2.7" xmlns="https://www.hamqth.com">
    <search> 
	<callsign>ok2cqr</callsign>
	<nick>Petr</nick> 
	<qth>Neratovice</qth> 
	<country>Czech Republic</country>
     	<adif>503</adif>
	<itu>28</itu> 
	<cq>15</cq> 
	<grid>jo70gg</grid> 
	<adr_name>Petr Hlozek</adr_name> 
	<adr_street1>17. listopadu 1065</adr_street1> 
	<adr_city>Neratovice</adr_city> 
	<adr_zip>27711</adr_zip> 
	<adr_country>Czech Republic</adr_country> 
     	<adr_adif>503</adr_adif>
	<district>GZL</district>
	<lotw>Y</lotw> 
	<qsl>Y</qsl> 
	<qsldirect>Y</qsldirect> 
	<eqsl>Y</eqsl> 
	<email>petr@ok2cqr.com</email>
	<jabber>petr@ok2cqr.com</jabber>
	<skype>PetrHH</skype> 
	<birth_year>1982</birth_year> 
	<lic_year>1998</lic_year> 
	<web>https://www.ok2cqr.com</web>
	<latitude>50.07</latitude>
	<longitude>14.42</longitude>
	<continent>EU</continent>
        <utc_offset>-1</utc_offset>
	<picture>https://www.hamqth.com/userfiles/o/ok/ok2cqr/_profile/ok2cqr_nove.jpg</picture>
    </search> 
    </HamQTH>
    """.strip()

class SearchCallsignNotFoundResponse:
    text = """
    <?xml version="1.0"?>
    <HamQTH version="2.7" xmlns="https://www.hamqth.com">
    <session>
      <error>Callsign not found</error>
    </session>
    </HamQTH>
    """.strip()


class SearchCallsignBioResponse:
    text = """
    <?xml version="1.0"?>
    <HamQTH version="2.7" xmlns="https://www.hamqth.com">
    <search> 
    <callsign>ok2cqr</callsign>
    <bio>my looong biography</bio> 
    </search> 
    </HamQTH>
    """.strip()


class SearchCallsignBioNotFoundResponse:
    text = """
    <?xml version="1.0"?>
    <HamQTH version="2.7" xmlns="https://www.hamqth.com">
    <session>
    <error>Callsign not found</error>
    </session>
    </HamQTH>
    """.strip()


class SearchCallsignRecentActivityResponse:
    text = """
    <?xml version="1.0"?>
    <HamQTH version="2.7" xmlns="https://www.hamqth.com">
    <search>
      <activity>
        <data>
          <source>DXC</source>
          <spotter>ZL2HAM</spotter>  
          <callsign>OK2CQR</callsign>
          <note>calling CQ</note>
          <freq>21025.0</freq>
          <date>2011-09-10</date>
          <time>05:34:28</time>
        </data>    
        <data>
          <source>RBN</source>
          <spotter>IK3STG</spotter>
          <callsign>OK2CQR</callsign>
          <note>13 dB  34 WPM  CQ</note>
          <freq>14026.3</freq>
          <date>2011-09-07</date>
          <time>13:34:28</time>
        </data>    
      </activity>
      <log_activity>
        <data>
          <callsign>PT0S</callsign>
          <band>20M</band>
          <mode>CW</mode>
          <date>2012-11-13</date>
        </data>
        <data>
          <callsign>OK1RR</callsign>
          <band>40M</band>
          <mode>CW</mode>
          <date>2012-09-07</date>
        </data>
      </log_activity>
      <logbook>
        <data>
          <callsign>AA3B</callsign>
          <band>15M</band>
          <mode>CW</mode>
          <date>2012-11-11</date>
        </data>
        <data>
          <callsign>OK7WA</callsign>
          <band>80M</band>
          <mode>SSB</mode>
          <date>2012-05-07</date>
        </data>
      </logbook>
    </search>
    </HamQTH>
    """.strip()


class SearchCallsignRecentActivityNotFoundResponse:
    text = """
    <?xml version="1.0"?>
    <HamQTH version="2.7" xmlns="https://www.hamqth.com">
      <session>
      <error>Callsign not found</error>
    </session>
    </HamQTH>
    """.strip()